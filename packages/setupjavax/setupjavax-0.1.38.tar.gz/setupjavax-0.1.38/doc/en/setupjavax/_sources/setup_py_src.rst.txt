
.. _SETUPPYSRC:

setup.py
--------
The *setup.py* of the *setupjavax* itself serves as a pattern for the provided libraries.
All *Python* projects of the author are based on the *setupjavax*,
some examples are:

* ePyUnit - [EPYUNIT]_ 
* filesysobjects - [FILESYSOBJECTS]_ 
* jsondata - [JSONDATA]_
* platformids - OS Type and Distribution IDs of System Platforms - [platformids]_
* platformids - [platformids]_ 
* pysourceinfo - [PYSOURCEINFO]_ 
* pythonids - Python Interpreter and Compiler IDs - [pythonids]_ 
* syscalls - [SYSCALLS]_


Custom
^^^^^^

For the commands provided by :ref:`setupjavax <SETUPLIB_COMMANDS>` refer to:

   +-----------------------------------------------+-------------------------------------------------+---------------------------------------+--------------------------------------------------------------+
   | summary                                       | cli options                                     | module                                | code                                                         |
   +===============================================+=================================================+=======================================+==============================================================+
   | :ref:`setup.py build_java <SETUP_BUILD_JAVA>` | :ref:`build_java <setuplibCOMMANDS_build_java>` | :ref:`build_java <setuplibBUILDJAVA>` | `BuildJava <_modules/setupjavax/build_java.html#BuildJava>`_ |
   +-----------------------------------------------+-------------------------------------------------+---------------------------------------+--------------------------------------------------------------+
   | :ref:`setup.py build_jy <SETUP_BUILD_JY>`     | :ref:`build_jy <setuplibCOMMANDS_build_jy>`     | :ref:`build_jy <setuplibBUILDJY>`     | `BuildJy <_modules/setupjavax/build_jy.html#BuildJy>`_       |
   +-----------------------------------------------+-------------------------------------------------+---------------------------------------+--------------------------------------------------------------+


Source
^^^^^^

.. literalinclude:: _static/setup.py
   :language: python
   :linenos:

Download
^^^^^^^^

`setup.py <_static/setup.py>`_

License
^^^^^^^
`Artistic-License-2.0 <_static/ArtisticLicense20.html>`_ + `Forced-Fairplay-Constraints <_static/licenses-amendments.txt>`_

Copyright
^^^^^^^^^
Copyright (C)2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

   