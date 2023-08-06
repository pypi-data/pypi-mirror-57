
*********
Blueprint
*********

.. _REFERENCE_ARCHITECTURE:



The modern landscapes of information infrastructures are commonly designed 
and organized as stacks of heterogeneous runtime environments
with comon frameworks.
A popular combination of components for the enterprise applications is the
application of *Python* in combnation with *Java* components and application servers.
The access to the *Java* modules is provided by the implementation *Jython*,
which integrates a seamless access to *Java* extensions including standard
*Java* libraries.
This supports the easy implementation of mixed components by modules implemented
in *Java* with modules implemented in *Pyhton*.

*Python* is designed to be compiled automatically on-the-fly during the execution
with the option of precompilation.
*Java* needs to be compiled before execution and relies during runtime solely on
the compiled libraries.
Thus the requirements for the packaging of a combined application comprising components of
both implementations is slightly different from a homogeneous *Python* application.

The *setupjavax* component provides hereby two additional commands *build_java* and *build_jy*.

.. _FIGURE_ARCHITECTURE:

.. figure:: _static/setuplib-architecture.png
   :figwidth: 250
   :align: center
   :target: _static/setuplib-architecture.png
   
   Figure: Setuplib Integration |setuplibarchitecture_zoom|

.. |setuplibarchitecture_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/setuplib-architecture.png
   :width: 16


* *build_jy* - for Jython:

  *build_jy* extends *build_py* by scan for and compilation of included *Java* modules. 

   .. parsed-literal::
   
      python :ref:`setup.py <SETUPPYSRC>` :ref:`build_jy <SETUP_BUILD_JY>`


* *build_java* - for Java:

  *build_java* introduces standalone *Java* modules. 

   .. parsed-literal::
   
      python :ref:`setup.py <SETUPPYSRC>` :ref:`build_java <SETUP_BUILD_JAVA>`

   
