from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from multiprocessing import Lock

import oss2
import six
from io import BytesIO
if six.PY2:
    from io import BytesIO as StringIO
else:
    from io import StringIO


class _OssIOBase(object):
    def __init__(self, bucket, path, buffer, *args, **kwargs):
        self._bucket = bucket
        self._path = path
        self._buffer = buffer

    @property
    def name(self):
        return "oss://" + "{}".format(self._bucket) + "/" + self._path.lstrip('/')

    def read(self):
        raise NotImplementedError()

    def write(self, val):
        raise NotImplementedError()

    def close(self):
        self.flush()
        self._buffer.close()

    def readable(self):
        raise NotImplementedError()

    def writable(self):
        raise NotImplementedError()

    def flush(self):
        raise NotImplementedError()

    def seek(self, val):
        raise NotImplementedError()

    def seekable(self):
        raise NotImplementedError()

    # def __getattr__(self, item):
    #     return getattr(self._buffer, item)

    def __repr__(self):
        return self.__class__.__name__ + "@" + self.name


class _OssReaderBase(_OssIOBase):
    def __init__(self, bucket, path, buffer, *args, **kwargs):
        super(_OssReaderBase, self).__init__(bucket, path, buffer, *args, **kwargs)
        self._buffer.write(bucket.get_object(path).read())
        self._buffer.seek(0)

    def read(self, *args, **kwargs):
        return self._buffer.read(*args, **kwargs)

    def write(self, val):
        raise IOError()

    def seek(self, *args, **kwargs):
        self._buffer.seek(*args, **kwargs)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def flush(self):
        self._buffer.seek(0)
        self._buffer.write(self._bucket.get_object(self._path).read())
        self._buffer.seek(0)


class _OssWriterBase(_OssIOBase):
    def __init__(self, bucket, path, buffer, *args, **kwargs):
        super(_OssWriterBase, self).__init__(bucket, path, buffer, *args, **kwargs)

    def read(self):
        raise IOError()

    def write(self, *args, **kwargs):
        b = self._buffer.write(*args, **kwargs)
        return b

    def readable(self):
        return False

    def writable(self):
        return True

    def flush(self):
        self._buffer.flush()
        self._buffer.seek(0)
        self._bucket.put_object(self._path, self._buffer.read())

    def seek(self, pos):
        if pos == 0:
            self._pos = 0
            self._buffer.seek(0)
        elif pos == 1:
            self._pos = self._bucket.get_object_meta(self._path)['Content-Length'] + 1
            self._buffer.seek(1)
        elif pos == 2:
            self._pos = self._bucket.get_object_meta(self._path)['Content-Length'] + 1
            self._buffer.seek(2)

    def seekable(self):
        return True


class OssBytesReader(_OssReaderBase):
    def __init__(self, bucket, path, *args, **kwargs):
        super(OssBytesReader, self).__init__(bucket, path, BytesIO(), *args, **kwargs)


class OssBytesWriter(_OssWriterBase):
    def __init__(self, bucket, path, *args, **kwargs):
        super(OssBytesWriter, self).__init__(bucket, path, BytesIO(), *args, **kwargs)

    def flush(self):
        if self._bucket.object_exists(self._path):
            self._bucket.delete_object(self._path)
        super(OssBytesWriter, self).flush()


class OssTextReader(_OssReaderBase):
    def __init__(self, bucket, path, *args, **kwargs):
        super(OssTextReader, self).__init__(bucket, path, StringIO(), *args, **kwargs)


class OssTextWriter(_OssWriterBase):
    def __init__(self, bucket, path, *args, **kwargs):
        super(OssTextWriter, self).__init__(bucket, path, StringIO(), *args, **kwargs)

    def flush(self):
        if self._bucket.object_exists(self._path):
            self._bucket.delete_object(self._path)
        super(OssTextWriter, self).flush()


class OssIOWrapper(object):
    def __init__(self, oss_session, ossio, fileno):
        self.file = oss_session
        self.io = ossio
        self._fileno = fileno

    def fileno(self):
        return self._fileno

    def close(self, fileno):
        self.file.close(fileno)

    def __enter__(self):
        return self.io

    def __exit__(self, type, value, traceback):
        self.close(self._fileno)

    def __getattr__(self, item):
        return getattr(self.io, item)


class OSSSession(object):
    def __init__(
            self,
            bucket,
            auth=None,
            access_id='your-access-id',
            access_key='your-access-key',
            endpoint='oss-cn-hangzhou.aliyuncs.com',
    ):
        self._bucket_name = bucket
        self._access_id = access_id
        self._access_key = access_key
        self._endpoint = endpoint

        if auth is None:
            auth = oss2.Auth(access_id, access_key)
        self._auth = auth
        self._bucket = oss2.Bucket(auth, endpoint, bucket)
        self._opened = []
        self._lock = Lock()

    def open(self, path, mode):
        if "+" in mode:
            raise NotImplementedError("Simultaneously reading and writing is not yet supported.")

        if len(mode) == 1:
            mode += "t"
        if mode == "rt":
            fp = OssTextReader(self._bucket, path)
        elif mode == "wt":
            fp = OssTextWriter(self._bucket, path)
        elif mode == "rb":
            fp = OssBytesReader(self._bucket, path)
        elif mode == "wb":
            fp = OssBytesWriter(self._bucket, path)
        elif mode == "at":
            raise NotImplementedError("Appending is not yet supported.")
        elif mode == "ab":
            raise NotImplementedError("Appending is not yet supported.")
        else:
            raise ValueError("Invalid mode pattern {}.".format(mode))

        with self._lock:
            self._opened.append(fp)
            fileno = len(self._opened) - 1
        return OssIOWrapper(self, fp, fileno=fileno)

    def close(self, fileno=None):
        with self._lock:
            if fileno is None:
                while len(self._opened) > 0:
                    self._opened.pop().close()
            else:
                self._opened.pop(fileno).close()

    @property
    def bucket(self):
        return self._bucket_name

    def __call__(self, *args, **kwargs):
        return self.open(*args, **kwargs)


if __name__ == '__main__':
    # import torch as th
    # from torch import nn
    from PIL import Image
    ossopen = OSSSession(
        "your-bucket",
        access_id="your-access-id",
        access_key="your-access-key",
        endpoint="oss-cn-hangzhou.aliyuncs.com"
    )
    with ossopen("path/to/your/img-file/without/bucket/name.jpg", "wb") as remote_fp:
        img = Image.open(remote_fp)
        with open("path/to/local/file.jpg", "wb") as local_fp:
            img.save(local_fp)
