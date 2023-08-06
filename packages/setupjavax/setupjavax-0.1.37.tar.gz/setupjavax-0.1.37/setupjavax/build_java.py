# -*- coding: utf-8 -*-
"""Compiles Java modules required for *Jython*.

Supports default standard paths only.

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

import distutils.cmd
import shutil

from yapyutils.files.finder import find_files
from setupjavax import SetupJavaXError


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1ba7bffb-c00b-4691-a3e9-e392f968e437"


class SetuplibBuildJavaError(SetupJavaXError):
    pass

class BuildJava(distutils.cmd.Command):
    """Compile Java modules for Jython."""

    description = 'Build Java modules for Jython.'
    user_options = [
        ('cp=',          None, "javac -cp <classpath>..."),
        ('deprecation',  None, "javac -deprecation ..."),
        ('g-all',        'g',  "javac -g ..."),
        ('jp=',          None, "javac -jar jython.jar -Dpython.path=<jp> ..."),
        ('nowarn',       None, "javac -nowarn ..."),
        ('source=',      None, "javac -source <release>..."),
        ('target=',      None, "javac -target <release>..."),
        ('verb',         "v", "javac -verbose..."),
        ('werror',       None, "javac -werror ..."),
        ('src',          None, "Copies sources, default is the *class* files only."),

        ('no-exec',      'n',  "print only, do not execute"),

    ]

    def initialize_options(self):
        self.cp = None
        self.deprecation = False
        self.g_all = None
        self.jp = None
        self.no_exec = None
        self.nowarn = False
        self.source = None
        self.src = False
        self.target = None
        self.verb = False
        self.werror = False

    def finalize_options(self):
        if self.no_exec != None:
            self.no_exec = True

    def run(self):
        """Run command."""
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

        if self.jp:
            command.append('-jp %s' % self.cp)

        exit_code = 0
        for pkg in sorted(self.distribution.packages):
            for f in sorted(find_files(pkg, '*.java')):
                call = ' '.join(command) + ' "' + str(f) + '"'
                print(call)

                if self.no_exec:
                    exit_code = 0
                else:
                    exit_code += os.system(call)
                    dst0 = "build" + os.sep + "lib" + os.sep + os.path.dirname(f)   
                    
                    if not os.path.exists(dst0):
                        print("make dir path: %s" % (dst0))
                        os.makedirs(dst0)
                    
                    if self.src:
                        print("copying source: %s -> %s" % (f, dst0))
                        shutil.copy(f, dst0)
                    
                    print("copying binary: %s -> %s" % (f[:-4] + "class", dst0))
                    shutil.copy(f[:-4] + "class", dst0)

        sys.exit(exit_code)
                
