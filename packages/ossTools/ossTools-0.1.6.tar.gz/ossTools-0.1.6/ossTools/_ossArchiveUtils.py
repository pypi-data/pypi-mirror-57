from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import contextlib
import ossTools
try:
    import tempfile
    import tarfile
except ImportError as exc:
    print("ossIO: ArchiveUtils is not available: {}".format(exc))


@contextlib.contextmanager
def working_directory(path):
    """A context manager which changes the working directory to the given
    path, and then changes it back to its previous value on exit.

    """
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


class OssArchiveWrapper(object):
    def __init__(self, archive_io):
        self.io = archive_io

    def __enter__(self):
        return self.io

    def __exit__(self, type, value, traceback):
        self.close()

    def __getattr__(self, item):
        return getattr(self.io, item)


class ossArchive(object):
    def __init__(self, path, cache_dir=None, oss_session=None):
        if oss_session is None:
            ossTools.__ossCheckInit()
            oss_session = ossTools.__OssHelper.oss_session
        bucket = oss_session._bucket
        self.archive = tarfile.open(fileobj=bucket.get_object(path), mode="r:*")

        if cache_dir is None:
            self.cache_dir = tempfile.TemporaryDirectory().name
        else:
            self.cache_dir = cache_dir

    def open(self, path, mode="r"):
        if "w" in mode or "+" in mode:
            raise ValueError("Writting is not suppurted by OSS API in stream mode.")
        with working_directory(self.cache_dir):
            file_obj = self.archive.extractfile(dict(zip(self.archive.getnames(), self.archive.getmembers()))[path])

        return OssArchiveWrapper(file_obj)
