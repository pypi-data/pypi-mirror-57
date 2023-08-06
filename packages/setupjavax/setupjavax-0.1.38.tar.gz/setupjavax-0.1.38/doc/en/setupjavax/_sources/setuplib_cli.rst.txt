
.. _SETUPLIBCOMMANDSCLI:

setup.py extensions by setupjavax
---------------------------------

The *setupjavax* provides the following extensions for the standard *setup.py* 
of the *setuptools* / *distutils*.
See :ref:`EXAMPLES <setupjavaxEXAMPLES>` for required integration steps, 
check integration with:

   .. parsed-literal::

      :ref:`python setup.py --help-commands <setuplibOPTIONS_help-commands>`.

Use new commands and options:

* *setup.py* extension commands:

   .. parsed-literal::
   
      :ref:`build_java <setuplibCOMMANDS_build_java>`      :ref:`build_jy <setuplibCOMMANDS_build_jy>`

* *setup.py* common global options:

   .. parsed-literal::

      :ref:`--sdk <setuplibOPTIONS_sdk>`
      :ref:`--no-install-requires <setuplibOPTIONS_no-install-requires>`    :ref:`--offline <setuplibOPTIONS_offline>`
      :ref:`--help-setupjavax <setuplibOPTIONS_help-setupjavax>`


.. _setuplibCLISYNOPSIS:

SYNOPSIS
^^^^^^^^
.. parsed-literal::

   setup.py :ref:`[Global-OPTIONS] <setupjavaxCLIOPTIONS>` :ref:`[COMMANDS-with-context-OPTIONS] <setuplibCOMMANDS>` 

.. _setuplibCLIOPTIONS:

OPTIONS
^^^^^^^

.. index::
   pair: options; --sdk
   pair: setupjavax; --sdk

.. _setuplibOPTIONS_sdk:

-\-sdk
""""""
Supports a separate dependency list for the build and packaging environment.
The following informal convention has to be implemented within the file *setup.py*.

   .. parsed-literal::
   
      __sdk = False
      """Set by the option "--sdk". Controls the installation environment."""
   
      if '--sdk' in sys.argv:
          _sdk = True
          sys.argv.remove('--sdk')
   
   
      _packages_sdk = find_packages(include=['setuplib'] )  # your development packages
      """Python packages to be installed."""
   
   
      if __sdk: # pragma: no cover
          _install_requires.extend(
              [
                  'sphinx >= 1.4',
                  'epydoc >= 3.0',
              ]
          )
   
          _packages = _packages_sdk

For an example refer to *setup.py* of *setuplib*.

.. index::
   pair: options; --no-install-requires
   pair: setuplib; --no-install-requires

.. _setuplibOPTIONS_no-install-requires:

-\-no-install-requires
""""""""""""""""""""""
Suppresses installation dependency checks,
requires appropriate PYTHONPATH.
The following informal convention has to be implemented within the file *setup.py*.

   .. parsed-literal::
   
      __no_install_requires = False
   
      if '--no-install-requires' in sys.argv:
          __no_install_requires = True
          sys.argv.remove('--no-install-requires')
   
   
      if __no_install_requires:
          print("#")
          print("# Changed to offline mode, ignore install dependencies completely.")
          print("# Requires appropriate PYTHONPATH.")
          print("# Ignored dependencies are:")
          print("#")
          for ir in _install_requires:
              print("#   "+str(ir))
          print("#")
          _install_requires=[]

For an example refer to *setup.py* of *setuplib*.

.. index::
   pair: options; --offline
   pair: setuplib; --offline

.. _setuplibOPTIONS_offline:

-\-offline
""""""""""
Sets online dependencies to offline, or ignores online
dependencies.
The following informal convention has to be implemented within the file *setup.py*.

   .. parsed-literal::
   
      __offline = False
   
      if '--offline' in sys.argv:
          __offline = True
          __no_install_requires = True
          sys.argv.remove('--offline')

For an example refer to *setup.py* of *setuplib*.

.. index::
   pair: options; --help-commands
   pair: setuplib; --help-commands

.. _setuplibOPTIONS_help-commands:

-\-help-commands
""""""""""""""""
The option '--help-commands' itself is not part of the *setuplib*, but it lists all
successfull integrated extension commands.
Thus the current extension commands has to be visible for validation. 

.. index::
   pair: options; --help-setuplib
   pair: setuplib; --help-setuplib

.. _setuplibOPTIONS_help-setuplib:

-\-help-setuplib
""""""""""""""""
Special help for *setuplib*.

For an example refer to *setup.py* of *setuplib*.

.. _setuplibCOMMANDS:

COMMANDS
^^^^^^^^

.. index::
   pair: commands; build_java
   pair: setuplib; build_java

.. _setuplibCOMMANDS_build_java:

build_java
""""""""""
Compiles java modules for 'Jython' and copies them into the *build* subtree.
The standard command 'build_py' has to be called extra.

.. warning::

   The mix of *Python* and *Java* modules within the same directory for the runtime 
   directories in particular in combination with an *__init__.py* / *__init__.pyc* is
   in case of *Jython* error prone.
   
   This is due to the required pre-scan of all packages within the startup initialization prologue
   by *Jython*.  Which is madatorily required in order to support *Python* reflection for 
   the *Java* packages.
   Thus seemingly the package path resolution prioritizes the *Python* resolution and therefore
   hides *Java* modules located within the same directory path. 
   Once these are split into a seperate directory path anything is fine.
   
   It seems to work in case of the *default* package within the global namespace,
   but this is due to the in any case required split not further thoroughly investigated. 

Creates for example in case of *platformids* [platformids]_ by default from 
the source-tree:

   .. parsed-literal::
   
      platformids
      └── jy
         └── dist
             └── nt
                 ├── Advapi32GetCurrentVersion.java
                 ├── Kernel32GetProductInfo.java
                 └── ReadCurrentVersionWinPrefs.java

the build tree with binaries only:

   .. parsed-literal::
   
      build/
      └── lib
          └── platformids
              └── jy
                  └── dist
                      └── nt
                          ├── Advapi32GetCurrentVersion.class
                          ├── Kernel32GetProductInfo.class
                          └── ReadCurrentVersionWinPrefs.class

The command supports a subset of the *javac* and *jython* options as convenience options.
For a complete set the commands has to be called direct.

.. _build_java_cp:

.. index::
   pair: build_java; --cp

-\-cp=
''''''
The classpath for the *Java* compiler.

Input:

   .. parsed-literal::
   
      setup.py build_java --cp=<classpath>

Java compiler call:

   .. parsed-literal::
   
      javac -cp <classpath> -jar /path/to/jython/jython.jar ...

The compilation of packages with platform support may for example require:

   .. parsed-literal::
   
      javac -cp %cd%;c:\\jna\\jna.jar;c:\\jna\\jna-platform.jar;c:\\jna\\win32-x86-64.jar -jar c:\\jython\\jython.jar ...

      javac -cp ${PWD}:/opt/jna/jna.jar:/opt/jna/jna-platform.jar:/opt/jna/win32-x86-64.jar -jar /opt/jython/jython.jar ...

.. _build_java_deprecation:

.. index::
   pair: build_java; -deprecation

-\-deprecation
''''''''''''''
Output source locations where deprecated APIs are used.

Input:

   .. parsed-literal::
   
      setup.py build_java --deprecation

Java compiler call:

   .. parsed-literal::
   
      javac -deprecation -jar /path/to/jython/jython.jar ...

.. _build_java_g:

.. index::
   pair: build_java; -g

-g
''
Generates complete debugging information for *java*.

Input:

   .. parsed-literal::
   
      setup.py build_java -g

Java compiler call:

   .. parsed-literal::
   
      javac -g-all -jar /path/to/jython/jython.jar ...
      javac -g     -jar /path/to/jython/jython.jar ...

.. _build_java_jp:

.. index::
   pair: build_java; --jp
   pair: build_java; -cp

-\-jp=
''''''
The sys.path/classpath for *Jython*.

Input:

   .. parsed-literal::
   
      setup.py build_java --jp=<jp>

Java compiler call:

   .. parsed-literal::
   
      javac  -jar /path/to/jython/jython.jar -Dpython.path <jp>...  # see [Jython]_


.. _build_java_noexec:

.. index::
   pair: build_java; -no-exec

-\-no-exec
''''''''''
Print only, do not execute.

   .. parsed-literal::
   
      javac --no-exec

.. _build_java_nowarn:

.. index::
   pair: build_java; -nowarn

-\-nowarn
'''''''''
Generate no warnings.

Input:

   .. parsed-literal::
   
      setup.py build_java --nowarn

Java compiler call:

   .. parsed-literal::
   
      javac -nowarn  -jar /path/to/jython/jython.jar ...

.. _build_java_source:

.. index::
   pair: build_java; -source

-\-source=
''''''''''
Provide source compatibility with specified release.

Input:

   .. parsed-literal::
   
      setup.py build_java --source=<release>

Java compiler call:

   .. parsed-literal::
   
      javac -source <release>  -jar /path/to/jython/jython.jar ...

.. _build_java_src:

.. index::
   pair: build_docx; --src

-\-src
''''''
Copies sources, default is the *class* files only:

   .. parsed-literal::
   
      setup.py build_docx --src

Creates for example in case of *platformids* [platformids]_ from 
the source-tree:

   .. parsed-literal::
   
      platformids
      └── jy
         └── dist
             └── nt
                 ├── Advapi32GetCurrentVersion.java
                 ├── Kernel32GetProductInfo.java
                 └── ReadCurrentVersionWinPrefs.java

the build tree with binaries and included sources:

   .. parsed-literal::
   
      build/
      └── lib
          └── platformids
              └── jy
                  └── dist
                      └── nt
                          ├── Advapi32GetCurrentVersion.class
                          ├── Advapi32GetCurrentVersion.java
                          ├── Kernel32GetProductInfo.class
                          ├── Kernel32GetProductInfo.java
                          ├── ReadCurrentVersionWinPrefs.class
                          └── ReadCurrentVersionWinPrefs.java
 
 .. _build_java_target:
 
.. index::
   pair: build_java; -target

-\-target=
''''''''''
Generate class files for specific VM version.

Input:

   .. parsed-literal::
   
      setup.py build_java --target=<release>

Java compiler call:

   .. parsed-literal::
   
      javac -target <release> -jar /path/to/jython/jython.jar ...

.. _build_java_verbose:

.. index::
   pair: build_java; -verbose

-\-verbose
''''''''''
Displays extra information 

Input:

   .. parsed-literal::
   
      setup.py build_java --verbose

Java compiler call:

   .. parsed-literal::
   
      javac -verbose -jar /path/to/jython/jython.jar ...

.. _build_java_werror:

.. index::
   pair: build_java; -werror

-\-werror
'''''''''
Terminate compilation if warnings occur.

Input:

   .. parsed-literal::
   
      setup.py build_java --werror

Java compiler call:

   .. parsed-literal::
   
      javac -Werror -jar /path/to/jython/jython.jar ...

.. index::
   pair: commands; build_jy
   pair: setuplib; build_jy

.. _setuplibCOMMANDS_build_jy:

build_jy
""""""""
Extends 'build_py' for compilation of Python and Java modules
for Jython.
Calls *build_py* and *build_java*, therefore provides a set of options for both.

   .. index::
      pair: build_jy; -cp
      pair: build_jy; --deprecation
      pair: build_jy; -g
      pair: build_jy; --jp
      pair: build_jy; --no-exec
      pair: build_jy; -no-exec
      pair: build_jy; --nowarn
      pair: build_jy; -nowarn
      pair: build_jy; --source
      pair: build_jy; -source
      pair: build_jy; --target
      pair: build_jy; -target
      pair: build_jy; --verbose
      pair: build_jy; -verbose
      pair: build_jy; --werror
      pair: build_jy; -werror

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +------------------+----------------------------------------------------------+---------------+
   | option           | reference command                                        |               |
   +==================+==========================================================+===============+
   | *-\-build-lib=*  | build_py --build-lib                                     | [setuptools]_ |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-compile*     | build_py --compile                                       | [setuptools]_ |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-cp=*         | :ref:`build_java --cp <build_java_cp>`                   |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-deprecation* | :ref:`build_java --deprecation <build_java_deprecation>` |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-force=*      | build_py --force                                         | [setuptools]_ |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-jp=*         | :ref:`build_java --jp <build_java_jp>`                   |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-no-compile*  | build_py --no-compile                                    | [setuptools]_ |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-no-exec*     | :ref:`build_java --no-exec <build_java_noexec>`          |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-nowarn*      | :ref:`build_java --nowarn <build_java_nowarn>`           |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-optimize=*   | build_py --optimize                                      | [setuptools]_ |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-source=*     | :ref:`build_java --source <build_java_source>`           |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-target=*     | :ref:`build_java --target <build_java_target>`           |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-verbose=*    | :ref:`build_java --verbose <build_java_verbose>`         |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-\-werror=*     | :ref:`build_java --werror <build_java_werror>`           |               |
   +------------------+----------------------------------------------------------+---------------+
   | *-g*             | :ref:`build_java -g <build_java_g>`                      |               |
   +------------------+----------------------------------------------------------+---------------+

   .. raw:: html
      
      </div>
      </div>
      </div>



DESCRIPTION
^^^^^^^^^^^

The call interface 'setuplib' provides command line extensions for 
the command line call interface of *setup.py*.

The curent version supports extension *commands*, future versions will
support *extension-points*.
 
.. _setuplibEXAMPLES:
 
EXAMPLES
^^^^^^^^

.. _examples:

0. Import in your :ref:`setup.py <SETUPPYSRC>` for example:

      ::
      
         #
         # setup extension modules
         #
         from setuplib import usage
         from setuplib.build_java import BuildJava
         from setuplib.build_docx import BuildDocX
         from setuplib.install_docx import InstallDocX
         from setuplib.testx import TestX
   
   
         class build_docx(BuildDocX):
             def __init__(self, *args, **kargs):
                 BuildDocX.__init__(self, *args, **kargs)
                 self.name = 'setuplib'                      # your package name
         
             
         class install_docx(InstallDocX):
             def __init__(self, *args, **kargs):
                 InstallDocX.__init__(self, *args, **kargs)
                 self.name = 'setuplib'                      # your package name
         
         
         class build_java(BuildJava):
             def __init__(self, *args, **kargs):
                 BuildJava.__init__(self, *args, **kargs)
                 self.name = 'setuplib'                      # your package name
         
         
         class testx(TestX):
             def __init__(self, *args, **kargs):
                 TestX.__init__(self, *args, **kargs)
                 self.name = 'setuplib'                      # your package name

1. Hook them in e.g. as a command in your :ref:`setup.py <SETUPPYSRC>` by:

      .. parsed-literal::
      
         setup(
             cmdclass={                           # see [setuppy]_
                 'build_java': build_java,
                 'build_docx': build_docx,
                 'install_docx': install_docx,
                 'testx': testx,
             },
             ...
         )


2. Use them from the command line call for example by:

      .. parsed-literal::
      
         python :ref:`setup.py <SETUPPYSRC>` :ref:`--help-setuplib <setuplibOPTIONS_help-setuplib>` 
         
         python :ref:`setup.py <SETUPPYSRC>` --help-commands           # see [setuppy]_ 
   
         python :ref:`setup.py <SETUPPYSRC>` :ref:`build_java <setuplibCOMMANDS_build_java>` --help 
   
         python :ref:`setup.py <SETUPPYSRC>` :ref:`build_java <setuplibCOMMANDS_build_java>`


SEE ALSO
^^^^^^^^
:ref:`setup.py <SETUPPYSRC>`, :ref:`setuplib <SETUPLIBCOMMANDSCLI>`,
[setuptools]_, [distutils]_


LICENSE
^^^^^^^
`Artistic-License-2.0 <_static/ArtisticLicense20.html>`_ + `Forced-Fairplay-Constraints <_static/licenses-amendments.txt>`_


COPYRIGHT
^^^^^^^^^
Copyright (C)2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
