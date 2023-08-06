setupjavax - Pre-Release
========================

**REMARK**: 

  This release is a nightly build for the The-Big-Bang integration test of 
  the whole set of currently released packages.
  Which together found parts of platform frameworks at the lower software stack.
  Thus naturally have some closer dependencies to their siblings.
  
  Even though applicable, *setupjavax* may have some integration issues, 
  and some options to be finalized.
  
  The final release is going to be available very soon. 


setupjavax
==========

The ‘setupjavax‘ package provides missing and enhanced extension modules for *setup.py* - setuptools / distutils. 
The current release supports the following commands, additional are coming soon:

* **build_java** - *Java* build and packaging for *Python*.

  Supports *Java* packaging for *Python* projects, adds native *Java* modules for *Jython*.

* **build_jy** - Integrated *Python* and *Java* builds for *Jython*.

  Supports combined *Java* and *Python* / *Jython* packaging. Calls *build_py* and *build_java*.

The current supported platforms are:

* Linux, BSD, Unix, OS-X, Cygwin, and Windows

* x86, amd64, arm32/armhf, arm64/aarch64

* Servers, Workstations, Embedded Systems

* Datacenters, public and private Clouds, IoT 

For more extensions refer to the online documentation.

**Online documentation**:

* https://pysetupjavax.sourceforge.io/

**Runtime-Repository**:

* PyPI: https://pypi.org/project/pysetupjavax/

  Install: *pip install setupjavax*, see also section 'Install' of the online documentation.


**Downloads**:

* sourceforge.net: https://sourceforge.net/projects/pysetupjavax/files/

* bitbucket.org: https://bitbucket.org/acue/pysetupjavax

* github.com: https://github.com/ArnoCan/pysetupjavax/

* pypi.org: https://pypi.org/project/pysetupjavax/


Project Data
------------

* PROJECT: 'setupjavax'

* MISSION: Command extension of *setup.py* for multi-platform and documentation deployments.

* VERSION: 00.01

* RELEASE: 00.01.038

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints

Concepts and enumeration values are migrated from the 

* *UnifiedSessionsManager* (C) 2008 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez.  

Runtime Environment
-------------------
For a comprehensive list refer to the documentation.

**Python Syntax Support**

*  Python2.7, and Python3

**Python Implementation Support**

*  CPython, IPython, IronPython, Jython, and PyPy

**OS on Server, Workstation, Laptops, Virtual Machines, and Containers**

* Linux: AlpineLinux, ArchLinux, CentOS, Debian, Fedora, Gentoo, OpenSUSE, Raspbian, RHEL, Slackware, SLES, Ubuntu, ...  

* BSD: DragonFlyBSD, FreeBSD, NetBSD, OpenBSD, GhostBSD, TrueOS, NomadBSD

* OS-X: Snow Leopard

* Windows: Win10, Win8.1, Win7, WinXP, Win2019, Win2016, Win2012, Win2008, Win2000

* WSL-1.0: Alpine, Debian, KaliLinux, openSUSE, SLES, Ubuntu

* Cygwin

* UNIX: Solaris10, Solaris11

* Minix: Minix3

* ReactOS

**Network and Security**

* Network Devices: OpenWRT

* Security: KaliLinux, pfSense

**OS on Embedded Devices**

* RaspberryPI: ArchLinux, CentOS, OpenBSD, OpenWRT, Raspbian

* ASUS-TinkerBoard: Armbian

**Creation of Special Deployment Packages**

* MicroPython: CircuitPython, MicroPython

Current Release
---------------

REMARK:
   Currently tested by application to the other projects of the author.
   So for now no package tests defined.

Major Changes:

* Initial version.

ToDo:

* Deployment to remote MicroPython, and CircuitPython

