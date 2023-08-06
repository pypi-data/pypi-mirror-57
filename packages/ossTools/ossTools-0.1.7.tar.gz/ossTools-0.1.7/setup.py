import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ossTools",
    version="0.1.7",
    description="Useful tools that simplify OSS file operation.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/allankevinrichie/ossTools",
    author="Suyue (Ziheng Zhang)",
    author_email="suyue.zzh@alibaba-inc.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ossTools"],
    include_package_data=True,
    install_requires=["oss2", "six"],
    extras_require={
        'archive-utils': ["tempfile", "tarfile"],
        'opencv-utils': ["opencv-python"],
        'tensorboard-utils': ["tensorboardX"]
    }
)
