from setuptools import setup, find_packages

setup(
  name='wcoin-wtech',
  version='1.0.0',
  description='The wcoin api',
  author='wangtry',
  author_email='wangtry3417@gmail.com',
  packages=find_packages(),
  install_requires=[
    requests
    # List any dependencies your package requires
  ],
)
