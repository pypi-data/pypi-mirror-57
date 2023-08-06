
*******
Cockpit
*******


Command Line Interface
----------------------

   Command extensions for *setup.py* - see also overview of :ref:`Setuplib Commands <SETUPLIB_COMMANDS>`.

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +--------------------------------------------------------------+-----------------------------+
   | Command Line Interface                                       | Call Options                |
   +==============================================================+=============================+
   | :ref:`setup.py \<setuplib-extensions> <SETUPLIBCOMMANDSCLI>` | :ref:`setuplibCLISYNOPSIS`  |
   +--------------------------------------------------------------+-----------------------------+
   |                                                              | :ref:`setupjavaxCLIOPTIONS` |
   +--------------------------------------------------------------+-----------------------------+
   |                                                              | :ref:`setupjavaxEXAMPLES`     |
   +--------------------------------------------------------------+-----------------------------+

   .. raw:: html
      
      </div>
      </div>
      </div>

API
---
For the common extensions interface:

   .. parsed-literal::
   
      python  setup.py <command> [<cli-options>]
      ipython setup.py <command> [<cli-options>]
      ipw.exe setup.py <command> [<cli-options>]
      jython  setup.py <command> [<cli-options>]
      pypy    setup.py <command> [<cli-options>]

refer to:

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">
   
   +--------------------------------------+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------------------------------+
   | commands                             | cli options                                              | module                                | API                                                                              |
   +======================================+==========================================================+=======================================+==================================================================================+
   | :ref:`build_jy <SETUP_BUILD_JY>`     | :ref:`setup.py build_jy <setuplibCOMMANDS_build_jy>`     | :ref:`build_java <setuplibBUILDJAVA>` | `setupjavax.build_java.BuildJava <_modules/setuplib/build_java.html#BuildJava>`_ |
   +--------------------------------------+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------------------------------+
   | :ref:`build_java <SETUP_BUILD_JAVA>` | :ref:`setup.py build_java <setuplibCOMMANDS_build_java>` | :ref:`build_jy <setuplibBUILDJY>`     | `setupjavax.build_jy.BuildJy <_modules/setuplib/build_jy.html#BuildJy>`_         |
   +--------------------------------------+----------------------------------------------------------+---------------------------------------+----------------------------------------------------------------------------------+
      
   .. raw:: html
      
      </div>
      </div>
      </div>
