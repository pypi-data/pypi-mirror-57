
.. _SETUPLIBEXTENSIONS: 


Setup Extensions
****************

Setuptools APIs
===============

The *setuptools* or *distutils* support the possibility of the exetnesion by additional
commands.
These support two flavours of APIs.

Extension Commands
------------------
Extension commands, or command classes are based on 

.. parsed-literal::

   distutils.cmd.Command
   
.. note::

   These work with *distutils* as well as with the newer *setuptools*.

The derived command classes define custom commands and add these to the internal dispatcher by inserting
the list of new commands into the setup call:

.. parsed-literal::

   setup(
       author="Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez",
       license="Artistic-License-2.0 + Forced-Fairplay-Constraints",
       cmdclass={
           'build_java': build_java,
           'build_jy': build_jy,
           'build_docx': build_docx,
           'install_docx': install_docx,
           'testx': testx,
       },
   )

Extension Points
----------------
Esxtension points are a newer interface, which also support background-registration
of the new comands for shared use.

This is not yet supported by *setupjavax*.


setupjavax
==========

Extension Classes
-----------------

.. _BUILDJAVA:

Build Java
""""""""""
Extension classes supporting the build, test, documentation, and packaging of integrated *Java*
packages.
This is in particular targeting *Jyhton* standalone, and in combination with the application servers
*JBoss*, *WebLogic*, and *WebSphere*.

   .. parsed-literal::

      :ref:`--sdk <setuplibOPTIONS_sdk>`

See :ref:`build_java <setuplibCOMMANDS_build_java>` and :ref:`build_jy <setuplibCOMMANDS_build_jy>`.


Global Options
--------------

Extension of shared functions for all commands currently provided by *setup.py*.

See :ref:`OPTIONS <setupjavaxCLIOPTIONS>`.
