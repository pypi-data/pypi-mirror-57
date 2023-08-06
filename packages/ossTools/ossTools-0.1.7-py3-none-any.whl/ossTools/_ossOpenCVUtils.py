from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import ossTools

try:
    import cv2
    import numpy as np
except ImportError as exc:
    print("ossIO: OpenCVUtils is not available: {}".format(exc))
import os.path


def imread(path, flags=cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH, oss_session=None):
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    with oss_session.open(path, "rb") as file_obj:
        img = cv2.imdecode(np.asarray(bytearray(file_obj.read())), flags=flags)
    return img


def imwrite(path, img, param=None, oss_session=None):
    ext = os.path.splitext(path)[1]
    if oss_session is None:
        ossTools.__ossCheckInit()
        oss_session = ossTools.__OssHelper.oss_session
    with oss_session.open(path, "wb") as file_obj:
        file_obj.write(cv2.imencode(ext, img.tobytes(), params=param))
