=======================
expi skel
=======================

-----------------------------------------------
Package Skeleton for the Extender Package Index
-----------------------------------------------


The ``expi_skel`` package provides a template for creating packages 
for the `Extender Package Index`_ (``expi``).  In addition to preconfigured
standard Python packaging files, such as ``setup.py`` and ``MANIFEST.in``,
the skeleton contains a sample ``expi.json`` file and ``vimodules/`` directory.

The ``expi.json`` file contains additional metadata about the package, such
as compatible Sage 300 and Orchid Extender versions, which Sage Views and
Screens are involved, and information on visibility and licensing.

The additional metadata enables ``expi`` to automatically generate package
landing pages and selectively serve packages only to authorized users. It
enables the `Python Package Manager for Extender`_ to perform
compatiblity checking so customizations are only ever installed on compatible 
systems.

.. _Extender Package Index: https://expi.2665093.ca
.. _Python Package Manager for Extender: https://2665093.ca/#extender-package-manager

The ``vimodules`` directory may contain Extender modules, ``*.vi`` files, that 
will be registered with Extender automatically after the Python package 
installation has completed.


