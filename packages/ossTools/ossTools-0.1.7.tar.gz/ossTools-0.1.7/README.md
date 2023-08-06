## Useful tools for OSS
Makes your experience with OSS easier.

### Quick start

```bash
pip install ossTools
```

**Caution: Currently, only the following functions are tested:**
- ossInit
- ossOpen
- imRead
- imWrite

Please report any problems with other untested functions to me, thanks!

Email: [Ziheng Zhang (Suyue)](mailto:suyue.zzh@alibaba-inc.com)

```python
from ossTools import *

ossInit(
        bucket='bucket-name',
        access_id='your-access-id',
        access_key='your-access-key',
        endpoint='oss-cn-hangzhou.aliyuncs.com',
)

# Read file, multiprocess safe!
with ossOpen("some/path/in/the/bucket", "r") as fp:
    print(fp.read())

# Write file, multiprocess safe!
with ossOpen("some/path/in/the/bucket", "w") as fp:
    # Python3
    print("Hello, world!", file=fp)
    # Python2
    fp.write("Hello, world!\n")

# Open and show an image with OpenCV
import cv2
# Use wrapped imRead/imWrite function in ossTools instead of cv2.imread
img = imRead("some/image.jpg", flags=cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
cv2.imshow("img", img)
cv2.waitKey()

# Integrate with tensorboardX
import tensorboardX as tb
writter = tb.SummaryWriter(log_dir="oss://bucket/path/to/oss/dir")
writter.add_scalar("train/loss", some_loss, global_step=iters)

# File Utils
# Check file existence
assert ossIsFile("path/to/file"), "File {} does not exist!".format("path/to/file")
# List files in a dir
print(ossListFile("path/to/dir"))
# Or list dirs in a dir
print(ossListDir("path/to/dir"))

# Download/Upload/Delete/Copy
ossDownloadFile("remote/path", "local/path", progress_callback=lambda per: print("{}% downloaded.".format(per)))
ossUploadFile("remote/path", "local/path", overwrite=True, progress_callback=lambda per: print("{}% uploaded.".format(per)))
ossDeleteFile("path/to/file")
ossDeleteDir("path/to/dir", iterative=True)
ossCopyFile("source/file", "target/file")
```