import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="microsoftgraph-python",
    version="1.2.0",
    description="API wrapper for Microsoft Graph written in Python",
    long_description=read("README.md"),
    url="https://github.com/GearPlug/microsoftgraph-python",
    long_description_content_type="text/markdown",
    author="Miguel Ferrer, Nerio Rincon, Yordy Gelvez",
    author_email="ingferrermiguel@gmail.com",
    license="MIT",
    packages=["microsoftgraph"],
    install_requires=[
        "requests",
        "msal==1.19.0",
    ],
    zip_safe=False,
)
