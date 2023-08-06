import codecs
from setuptools import setup

long_description = codecs.open('README.rst', "r").read()

setup(
    name="gdshortener",
    version="1.0.0",
    author="Gian Luca Dalla Torre",
    author_email="gianluca@gestionaleauto.com",
    description=("A module that provides access to .gd URL Shortener"),
    license="LGPL",
    keywords="url shortener gd",
    url="https://github.com/torre76/gd_shortener",
    download_url="https://github.com/torre76/gd_shortener/tarball/1.0.0",
    packages=['gdshortener'],
    long_description=long_description,
    package_data={
        '': ['README.rst'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        "requests >= 2.21.0"
    ]
)
