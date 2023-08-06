from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import oss2

import ossTools


MULTIPART_THRESHOLD = 10 * 1024 * 1024


def ossDeleteFile(path, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    bucket.delete_object(path)


def ossDeleteDir(path, iterative=True, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    for obj in oss2.ObjectIterator(bucket, prefix=path, delimiter="" if iterative else "/"):
        bucket.delete_object(obj.key)


def ossCopyFile(src_path, obj_path, part_size=1024 * 1024, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools._OssHelper.oss_session
    bucket = oss_session._bucket

    src_object = src_path
    dst_object = obj_path

    total_size = bucket.head_object(src_object).content_length

    if total_size < MULTIPART_THRESHOLD:
        return [1, bucket.copy_object(bucket.bucket_name, src_path, obj_path)]

    # initialize parts
    upload_id = bucket.init_multipart_upload(dst_object).upload_id
    parts = []

    # copy parts
    part_number = 1
    offset = 0
    while offset < total_size:
        num_to_upload = min(part_size, total_size - offset)
        byte_range = (offset, offset + num_to_upload - 1)

        result = bucket.upload_part_copy(bucket.bucket_name, src_object, byte_range, dst_object, upload_id, part_number)
        parts.append((part_number, result.etag))

        offset += num_to_upload
        part_number += 1

    # complete copy
    bucket.complete_multipart_upload(dst_object, upload_id, parts)

    return parts


def ossDownloadFile(remote_path, local_path, progress_callback=None, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket

    return oss2.resumable_download(bucket, remote_path, local_path, progress_callback=progress_callback,
                                   multipart_threshold=MULTIPART_THRESHOLD)


def ossUploadFile(remote_path, local_path, overwrite=False, progress_callback=None, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    bucket = oss_session._bucket
    if ossTools.ossIsDir(remote_path, oss_session):
        raise IOError("Dir already exists: {}".format(remote_path))
    elif ossTools.ossIsFile(remote_path, oss_session):
        if not not overwrite:
            raise IOError(
                "File already exists: {}, please explicitly set overwrite=True to overwrite.".format(remote_path))
        ossDeleteFile(remote_path, oss_session)

    oss2.resumable_upload(bucket, remote_path, local_path, progress_callback=progress_callback,
                          multipart_threshold=MULTIPART_THRESHOLD)
