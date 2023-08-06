
********
Abstract
********

Modern landscapes of information infrastructures are commonly designed 
and organized as stacks of runtime service environments.
The technical architecture of the service stacks consists of a wide range of
heterogenous landscapes of components frequently requiring adaptation and mediation
with extended special installations by *setuptools* / *distutils* via *setup.py*.
This frequently requires the integration of components implemented of multiple programming languages.
A popular component for the integration of *Python* and *Java* is *Jython* [Jython]_ with support of intermixed
modules.
*Jython* extensions are supported by various *Java* based application servers, 
e.g.  by *JBoss Application Server*, *Oracle Weblogic Server*, and *IBM WebSphere Application Server*.

The *Jython* implementation requires frequently compiled native *Java* modules as extentions, which require to be
compiled and packaged in combination with *Python* modules for distribution.

.. figure:: _static/systems-ids.png
   :figwidth: 400px
   :align: center
   :target: _static/systems-ids.png
   
   Figure: Installation of Service Layers |figuresystemabstractprint_zoom| :ref:`more... <REFERENCE_ARCHITECTURE>`

.. |figuresystemabstractprint_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/systems-ids.png
   :width: 16

The *setupjavax* supports commands for the compilation and packaging of *Java* packages in conjunction with *Jython*.

For tested standard OS and distributions see help
on `installation <install.html>`_ / :ref:`Tested OS and Python Implementations <TESTED_OS_PYTHON>`.
