from __future__ import print_function
from __future__ import absolute_import
from __future__ import division


import ossTools
import copy
import io

record_writer = None

try:
    from tensorboardX import record_writer
    record_writer.OSS_ENABLED = True
except ImportError as exc:
    print("ossIO: TensorBoard is not available: {}".format(exc))
    record_writer.OSS_ENABLED = False


class OSSRecordWriter(object):
    """Writes tensorboard protocol buffer files to OSS."""

    def __init__(self, path, oss_session=None):
        if oss_session is None:
            ossTools.__ossCheckInit()
            self.oss_session = ossTools.__OssHelper.oss_session
        else:
            self.oss_session = oss_session
        self.buffer = io.BytesIO()
        self.path = path

    def __del__(self):
        self.close()

    def bucket_and_path(self):
        path = self.path
        if path.startswith("oss://"):
            path = path[len("oss://"):]
        bp = path.split("/")
        bucket = bp[0]
        path = path[1 + len(bucket):]
        return bucket, path

    def write(self, val):
        self.buffer.write(val)

    def flush(self):
        bucket, path = self.bucket_and_path()
        upload_buffer = copy.copy(self.buffer)
        upload_buffer.seek(0)
        assert self.oss_session.bucket == bucket, "Bucket: {} is not initialized in this session.".format(bucket)
        with self.oss_session.open(path, "wb") as fp:
            fp.write(upload_buffer.read())

    def close(self):
        self.flush()


if record_writer.OSS_ENABLED:
    record_writer.register_writer_factory("oss", OSSRecordWriter)
