from setuptools import setup, find_packages

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(
  name='wcoin-wtech',
  url="https://github.com/wangtry3417/wcoin.git
  version='1.0.0',
  description='The wcoin api',
  long_description=readme,
  license='MIT',
  author='wangtry',
  author_email='wangtry3417@gmail.com',
  packages=find_packages(),
  install_requires=[
    requests
    # List any dependencies your package requires
  ],
 classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
