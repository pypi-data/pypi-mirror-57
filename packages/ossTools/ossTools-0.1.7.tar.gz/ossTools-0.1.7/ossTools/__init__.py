from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

__author__ = ("suyue (Ziheng Zhang) <suyue.zzh@alibaba-inc.com>")
__all__ = ("ossInit", "ossIsInitialized", "OSSSession", "ossOpen",
           "ossArchive",
           "imRead", "imWrite",
           "ossListFile", "ossListDir", "ossIsDir", "ossIsFile",
           "ossDeleteFile", "ossDeleteDir", "ossCopyFile", "ossDownloadFile", "ossUploadFile"
           )
__version__ = "0.1.7"


import oss2

from ._ossIO import OSSSession
from ._ossArchiveUtils import ossArchive
from ._ossOpenCVUtils import imwrite as imWrite, imread as imRead
from ._ossPath import ossListFile, ossListDir, ossIsDir, ossIsFile
from ._ossFile import ossDeleteFile, ossDeleteDir, ossCopyFile, ossDownloadFile, ossUploadFile
from . import _ossTensorBoardUtils


class __OssHelper(object):
    oss_auth = None
    oss_session = None
    bucket_name = ""
    access_id = None
    access_key = None
    endpoint = None


def ossOpen(path, mode):
    __ossCheckInit()
    return __OssHelper.oss_session(path, mode)


def ossInit(
        bucket,
        access_id='your-access-id',
        access_key='your-access-key',
        endpoint='oss-cn-hangzhou.aliyuncs.com',
):
    __OssHelper.oss_auth = oss2.Auth(access_id, access_key)
    __OssHelper.oss_session = OSSSession(bucket, auth=__OssHelper.oss_auth, endpoint=endpoint)
    __OssHelper.access_id = access_id
    __OssHelper.access_key = access_key
    __OssHelper.endpoint = endpoint
    __OssHelper.bucket_name = bucket

    return __OssHelper.oss_auth, __OssHelper.oss_session


def ossClose():
    if __OssHelper.oss_auth is None:
        return
    __OssHelper.oss_session.close()


def ossGetAuth():
    __ossCheckInit()
    return __OssHelper.oss_auth


def ossGetSession():
    __ossCheckInit()
    return __OssHelper.oss_session


def ossIsInitialized():
    return __OssHelper.oss_auth is not None


def __ossCheckInit():
    if not ossIsInitialized():
        raise RuntimeError("OSS session not initialized, please call 'ossInit' first.")
