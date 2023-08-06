# -*- coding: utf-8 -*-=

from setuptools import find_packages
from setuptools import setup

with open("README.pypi.md", "r") as fh:
    long_description = fh.read()

setup(
    name="certbot_dns_isset",
    version="0.0.2",
    author="Gerben Geijteman",
    author_email="gerben@isset.nl",
    description="Certbot plugin for Isset DNS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://isset.nl/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'certbot',
        'zope.interface',
    ],
    entry_points={
        'certbot.plugins': [
            'dns-isset = certbot_dns_isset.dns_isset:Authenticator',
        ],
    },
)
