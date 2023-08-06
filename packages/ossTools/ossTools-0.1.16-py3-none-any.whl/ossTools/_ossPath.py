from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import oss2

import ossTools


def ossListFile(path, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    path = path.rstrip("/") + "/"
    files = filter(lambda obj: not obj.is_prefix(), oss2.ObjectIterator(bucket, prefix=path, delimiter="/"))
    next(files)
    return [_.key.split("/")[-1] for _ in files]


def ossListDir(path, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    path = path.rstrip("/") + "/"
    return [_.key.split("/")[-2] for _ in filter(lambda obj: obj.is_prefix(), oss2.ObjectIterator(bucket, prefix=path, delimiter="/"))]


def ossIsDir(path, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    # if not bucket.object_exists(path):
    #     return False
    for obj in oss2.ObjectIterator(bucket, prefix=path.rstrip("/"), delimiter='/'):
        if obj.is_prefix():
            return True
    return False


def ossIsFile(path, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    if not bucket.object_exists(path):
        return False
    for obj in oss2.ObjectIterator(bucket, prefix=path):
        return not obj.is_prefix()
