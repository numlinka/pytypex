# Licensed under the MIT License.
# pytypex Copyright (C) 2022 numlinka.
# setup

# site
from setuptools import setup


setup(
    name = "typex",
    version = "0.2.0",
    description = "Python fundamental type extension.",
    long_description = open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    author = "numlinka",
    author_email = "numlinka@163.com",
    url = "https://github.com/numlinka/pytypex",
    package_dir={"": "src"},
    py_modules=["typex"],
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    license = "MIT",
    keywords = ["type", "class", "static", "singleton", "multiton", "atomic"],
    install_requires = []
)
