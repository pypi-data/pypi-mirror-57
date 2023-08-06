from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import oss2

import ossTools


def ossListFile(path, iterative=False, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    return filter(lambda obj: not obj.is_prefix(), oss2.ObjectIterator(bucket, prefix=path, delimiter="" if iterative else "/"))


def ossListDir(path, iterative=False, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    return filter(lambda obj: obj.is_prefix(), oss2.ObjectIterator(bucket, prefix=path, delimiter="" if iterative else "/"))


def ossIsDir(path, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    if not bucket.object_exists(path):
        return False
    for obj in oss2.ObjectIterator(bucket, prefix=path):
        return obj.is_prefix()


def ossIsFile(path, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    if not bucket.object_exists(path):
        return False
    for obj in oss2.ObjectIterator(bucket, prefix=path):
        return not obj.is_prefix()
