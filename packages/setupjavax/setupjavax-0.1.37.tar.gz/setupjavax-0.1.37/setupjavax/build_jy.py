# -*- coding: utf-8 -*-
"""Compiles Python and Java modules required for *Jython*.

Supports default standard paths only.

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

# REMINDER: import distutils.cmd
import setuptools.command.build_py
import shutil

from yapyutils.files.finder import find_files
from setupjavax import SetupJavaXError


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1ba7bffb-c00b-4691-a3e9-e392f968e437"


class SetuplibBuildJyError(SetupJavaXError):
    pass

# REMINDER: class BuildJy(distutils.cmd.Command):
class BuildJy(setuptools.command.build_py.build_py):
    """Extends 'build_py' for compilation of Python and Java modules
    for Jython.
    """

    description = 'Build Python and Java modules for Jython.'
    user_options = setuptools.command.build_py.build_py.user_options + [
        ('build-lib=',   None, "build_py --build-lib="),
        ('compile',      None, "build_py --compile"),
        ('cp=',          None, "javac -cp <classpath>..."),
        ('deprecation',  None, "javac -deprecation ..."),
        ('force',        None, "build_py --force"),
        ('g-all',        'g',  "javac -g ..."),
        ('jp=',          None, "javac -jar jython.jar -Dpython.path=<jp> ..."),
        ('no-compile',   None, "build_py --no-compile"),
        ('no-exec',      None, "print only"),
        ('nowarn',       None, "javac -nowarn ..."),
        ('optimize',     None, "build_py --optimize"),
        ('source=',      None, "javac -source <release>..."),
        ('target=',      None, "javac -target <release>..."),
        ('verb',         "v", "javac -verbose..."),
        ('werror',       None, "javac -werror ..."),
    ]

    def initialize_options(self):
        setuptools.command.build_py.build_py.initialize_options()
        
        self.cp = None
        self.deprecation = False
        self.g_all = None
        self.nowarn = False
        self.source = None
        self.target = None
        self.verb = False
        self.verbose = None
        self.werror = False

    def finalize_options(self):
        setuptools.command.build_py.build_py.finalize_options()
        
        pass

    def run(self):
        """Run command."""

        setuptools.command.build_py.build_py.run()

        command = [
            'javac'
        ]

        if self.deprecation:
            command.append('-deprecation')
        if self.nowarn:
            command.append('-nowarn')
        if self.werror:
            command.append('-werror')
    
        if self.verb:
            command.append('-verbose')
        if self.g_all:
            command.append('-g')
        if self.cp:
            command.append('-cp %s' % self.cp)
        if self.source:
            command.append('-source %s' % self.source)
        if self.target:
            command.append('-target %s' % self.target)

        exit_code = 0
        for pkg in sorted(self.distribution.packages):
            for f in sorted(find_files(pkg, '*.java')):
                call = ' '.join(command) + ' "' + str(f) + '"'
                print(call)
                exit_code += os.system(call)
                dst0 = "build" + os.sep + "lib" + os.sep + os.path.dirname(f)   
                print("copying %s -> %s" % (f, dst0))
                if not os.path.exists(dst0):
                    os.makedirs(dst0)
                shutil.copy(f, dst0)
                print("copying %s -> %s" % (f[:-4] + "class", dst0))
                shutil.copy(f[:-4] + "class", dst0)

        sys.exit(exit_code)
                
