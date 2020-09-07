# Ckandr

from setuptools import setup

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """
About
-----
kupectx is a context management command-line utility for Kubernetes.

Usage
-----
Check out help:

::

    $ kupectx --help

    """

setup(
    name = 'kupectx',
    packages = ['kupectx'],
    #install_requires = ['certifi==2017.11.5', 'chardet==3.0.4', 'idna==2.6', 'requests==2.18.4', 'terminaltables==3.1.0', 'urllib3==1.22'],
    version = '0.1',
    license = 'MIT',
    description = 'Command-line utility for Kubernetes context management',
    long_description= long_description,
    author = 'Raseel Bhagat',
    author_email = 'raseelbhagat@gmail.com',
    url = 'https://github.com/screwgoth/kupectx',
    download_url = 'https://github.com/screwgoth/kupectx/archive/0.1.tar.gz',
    entry_points={
        'console_scripts': ['kupectx=kupectx.main:main'],
    },
    keywords = 'kubernetes python cli command-line',
    classifiers = [
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: End Users/Desktop',
      'License :: OSI Approved :: MIT License',
      'Operating System :: MacOS',
      'Operating System :: POSIX',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.8',
      'Topic :: Utilities'
      ],
)
