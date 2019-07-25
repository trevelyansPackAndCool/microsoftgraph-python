import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='microsoftgraph-python',
      version='0.1.5',
      description='API wrapper for Microsoft Graph written in Python',
      long_description=read('README.md'),
      url='https://github.com/GearPlug/microsoftgraph-python',
      author='Miguel Ferrer, Nerio Rincon, Yordy Gelvez',
      author_email='ingferrermiguel@gmail.com',
      license='GPL',
      packages=['microsoftgraph'],
      install_requires=[
          'requests',
          'msal==0.5.1'
      ],
      zip_safe=False)
