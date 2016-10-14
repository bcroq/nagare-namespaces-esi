# --
# Copyright (c) 2008-2013 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import os.path

from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version:
    VERSION = version.readline().rstrip()

setup(
    name='nagare-namespaces-esi',
    version=VERSION,
    author='Alain Poirier',
    author_email='alain.poirier at net-ng.com',
    description='Nagare Python web framework - namespaces.esi',
    license='BSD',
    url='http://www.nagare.org',
    download_url='http://www.nagare.org/download',
    packages=find_packages(),
    namespace_packages=('nagare.namespaces', ),
    dependency_links=('http://www.nagare.org/download/', ),
    install_requires=('nagare-namespaces', ),
    extras_require={
        'test': ('nose', )
    },
    test_suite='nose.collector'
)
