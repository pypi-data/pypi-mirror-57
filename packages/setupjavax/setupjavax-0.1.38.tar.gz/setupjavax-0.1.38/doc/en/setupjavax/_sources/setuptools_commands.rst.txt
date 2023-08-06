

.. _SETUPLIB_COMMANDS:


Setuplib Commands
=================

Java Build Commands
-------------------

.. _SETUP_BUILD_JAVA:

build_java
^^^^^^^^^^
The *build_java* command extension supports the build of *Java* modules within the 
*Python* distribution tree.
Therefore the provided package directories are scanned for *\*.java* files,
which are compiled and copied into the *build* subtree.
These are than included into the distribution transparently by the choosen packer.

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +-------------+--------------------------------------------------------------------------------+
   | CLI command | :ref:`build_java <setuplibCOMMANDS_build_java>`                                |
   +-------------+--------------------------------------------------------------------------------+
   | API class   | `setuplib.build_java.BuildJava <_modules/setuplib/build_java.html#BuildJava>`_ |
   +-------------+--------------------------------------------------------------------------------+

   .. raw:: html
      
      </div>
      </div>
      </div>

.. _SETUP_BUILD_JY:

build_jy
^^^^^^^^
The command *build_jy* combines the standard command *build_py* with the 
extension command *build_java* and generates the *build* tree for both by one call. 


   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +-------------+------------------------------------------------------------------------+
   | CLI command | :ref:`build_jy <setuplibCOMMANDS_build_jy>`                            |
   +-------------+------------------------------------------------------------------------+
   | API class   | `setuplib.build_jy.BuildJy <_modules/setuplib/build_jy.html#BuildJy>`_ |
   +-------------+------------------------------------------------------------------------+

   .. raw:: html
      
      </div>
      </div>
      </div>
