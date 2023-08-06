Abstract
========

The *namedtupledefs* package provides a patched version of the original *collections.namedtuple*.
The *namedtupledefs* package introduces: 

* *field defaults*

   Default values for the fields in function style see [PYFUNC]_
   The implementation is pure dynamic by generated default values for the method *__new__*, thus has 
   no impact on the created *namedtuple* class. Neither on resources, nor on performance.
   See :ref:`API_NEW`. 

* *merge*

   In addition the method *_merge* is added to the created named tuple class.
   This provides the concatination of multiple results from *namedtuple* into a
   new instance of a new class. See :ref:`API_MERGE`, :ref:`Python2 <CODE_PYTHON2>`,
   and :ref:`Python3 <CODE_PYTHON3>`. 


.. _FIGURE_STRUCTURE:

.. figure:: _static/structure.png
   :figwidth: 650
   :align: center
   :target: _static/structure.png
   
   Figure: Class Diagram of namedtupledefs |structure_zoom| :ref:`more... <REFERENCE_ARCHITECTURE>`

.. |structure_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/structure.png
   :width: 16

For an overview with additional details refer to the following section :ref:`Blueprint <INDEX_BLUEPRINT>`.

For the standard library *collections.namedtuple* see Python documentation [namedtuple]_.
For the release for Python2 refer to 
*namedtupledefs2* [namedtupledefs2]_.
