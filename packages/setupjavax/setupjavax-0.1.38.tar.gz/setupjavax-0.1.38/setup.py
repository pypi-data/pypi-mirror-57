# -*- coding: utf-8 -*-
"""Distribute 'setupjavax', multi-platform support for regression tests.

Additional local options for this *setup.py* module:
   --no-install-requires: 
       Suppresses installation dependency checks,
       requires appropriate PYTHONPATH.

   --offline: 
       Sets online dependencies to offline, or ignores online
       dependencies.

"""
from __future__ import absolute_import
from __future__ import print_function

try:
    # optional remote debug
    from rdbg import start        # load a slim bootstrap module
    start.start_remote_debug()    # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass


import os
import sys

import setuptools


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1ba7bffb-c00b-4691-a3e9-e392f968e437"

__vers__ = [0, 1, 38, ]
__version__ = "%02d.%02d.%03d" % (__vers__[0], __vers__[1], __vers__[2],)
__release__ = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],) + '-rc0'
__status__ = 'beta'


__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    __sdk = True
    sys.argv.remove('--sdk')


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


_name = 'setupjavax'
__pkgname__ = "setupjavax"
_version = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],)


_install_requires = [
    'pythonids >= 0.1.31',
    'yapyutils >= 0.1.0',
    'yapydata >= 0.1.0',
    'sourceinfo >= 0.1.0',
]


__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')


if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   " + str(ir))
    print("#")
    _install_requires = []


#
# see setup.py for remaining parameters
#
setuptools.setup(
    author=__author__,
    author_email=__author_email__,
    description="Support Java extensions for setuptools / distutils.",
    download_url="https://sourceforge.net/projects/setupjavax/files/",
    entry_points={                    # for standard application
        'distutils.commands': 'build_java = setupjavax.build_java:BuildJava',
        'distutils.commands': 'build_jy = setupjavax.build_jy:BuildJy',
    },
    install_requires=_install_requires,
    license=__license__,
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    name=_name,
    packages=['setupjavax',],
    scripts=[],
    url='https://sourceforge.net/projects/setupjavax/',
    version=_version,
    zip_safe=False,
)


if '--help' in sys.argv or '-h' in sys.argv:
    print()
    print("Help on usage extensions by " + str(_name))
    print("   --help-" + str(_name))
    print()

sys.exit(0)

