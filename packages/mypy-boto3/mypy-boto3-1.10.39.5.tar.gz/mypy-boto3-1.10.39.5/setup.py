import os
from os.path import abspath, dirname

from setuptools import setup


LONG_DESCRIPTION = open(dirname(abspath(__file__)) + "/README.md", "r").read()


setup(
    name="mypy-boto3",
    version="1.10.39.5",
    packages=["mypy_boto3",],
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Mypy-friendly boto3 1.10.39 type annotations master module.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=["boto3", "typing_extensions; python_version < '3.8'",],
    package_data={"mypy_boto3": ["py.typed"]},
    zip_safe=False,
    entry_points={"console_scripts": ["mypy_boto3 = mypy_boto3.main:main"]},
)
