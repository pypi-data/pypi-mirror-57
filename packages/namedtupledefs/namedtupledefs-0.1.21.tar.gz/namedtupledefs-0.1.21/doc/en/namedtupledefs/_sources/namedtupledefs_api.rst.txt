
.. _namedtupledefsAPI:

The namedtupledefs API
**********************
The *namedtupledefs* API covers a variety of interfaces for the processing of 
resource path addresses, and the search of resources.
The initial set of interfaces forcusses on filesystem resources in a basic distributed
environment.
This covers in particular a basic set of call parameters, which are common for a
subset of the call interfaces. 


API
---
Interfaces
^^^^^^^^^^

.. _IF_FACTORIES:

.. raw:: html
   
   <style>
      div.apisynopsislarge blockquote {
         font-size: 1.5ch;
      }
   </style>
   
   <div class="apisynopsislarge">
   <div class="apisynopsis">

* **factory functions**

   .. parsed-literal::
   
      :ref:`namedtuple <API_namedtuple>`
   
.. raw:: html

   </div>
   </div>

Class Options by Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _API_PARAMS_BASIC::

Basic Application API
"""""""""""""""""""""
The following table displays the parameters supported by the interfaces.

   .. raw:: html
   
      <div class="tabcolumncolor">
      <div class="nonbreakheadtab">
      <div class="autocoltab">
         
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
   | interface                                      | collections.namedtuple        | :ref:`namedtupledefs.namedtuple <API_namedtuple>` |
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
   | parameters                                     | [namedutple-python3]_         |                                                   |
   +================================================+===============================+===================================================+
   | :ref:`fieldnames <param_fieldnames>`           | :ref:`c <RETURN_namedtuple>`  | :ref:`c <RETURN_namedtuple>`                      |
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
   | :ref:`fielddefaults <param_fielddefaults>` (1) | :ref:`-- <RETURN_namedtuple>` | :ref:`c <RETURN_namedtuple>`                      |
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
   | :ref:`module <param_module>` (2)               | :ref:`c <RETURN_namedtuple>`  | :ref:`c <RETURN_namedtuple>`                      |
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
   | :ref:`rename <param_rename>`                   | :ref:`c <RETURN_namedtuple>`  | :ref:`c <RETURN_namedtuple>`                      |
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
   | :ref:`typename <param_typename>`               | :ref:`c <RETURN_namedtuple>`  | :ref:`c <RETURN_namedtuple>`                      |
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
   | :ref:`verbose <param_verbose>`                 | :ref:`c <RETURN_namedtuple>`  | :ref:`c <RETURN_namedtuple>`                      |
   +------------------------------------------------+-------------------------------+---------------------------------------------------+
         
      .. raw:: html
      
         </div>
         </div>
         </div>
      
      **c**:
   
      Parameter as call parameters.
      For example the parameters **rename** and **fielddefaults** are used by
      the factory *namedtupledefs.namedtuple()* for the creation of the extended tuple
      class template as well as for the creation of the class. 
      E.g.:
      
         .. parsed-literal::
         
            namedtupledefs.abc.namedtupledefs(
               'MyClass',                              # processed by *namedtuple* 
               ('a', 'b',),                            # processed by *namedtuple*
               rename=True,                            # processed by *namedtuple*
               fielddefaults=(11, 22)                  # processed by **__new__** for class and instance creation
            )
   
   **(1)**:
      Depends on the actual *tuplefactory*.

   **(2)**:
      Depends on the implementation, *Python3.6+*.

.. _namedtupledefsAPI_PARAMETERS:

Parameters
""""""""""



.. index::
   pair: parameters; fieldnames
   pair: parameters; _fieldnames

.. _param_fieldnames:

fieldnames
''''''''''
Symbolic names of fields with identical semantics as the standard library *collections.namedtuple*.
When used in combination with the parameter *fielddefaults* the semantics changes to the behaviour
of function parameters with default values, see [PYFUNC]_.  

   .. parsed-literal::

      fieldnames := '(' <field-name> [, <fieldnames>] ')'
      field-name := <valid-character-one>[<field-name-tail>] 
      field-name-tail := <valid-character>[<field-name-tail>]
      valid-character-one := [a-zA-Z] 
      valid-character := [a-zA-Z_0-9] 

See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.


.. index::
   pair: parameters; _fielddefaults
   pair: parameters; fielddefaults

.. _param_fielddefaults:

fielddefaults
'''''''''''''
Optional support for default values of *fieldnames*.
A list of values.
Same semantics as the function call interfaces [PYFUNC]_,

   .. parsed-literal::

      fielddefaults := '(' <item-default> [, <fielddefaults>] ')'
      item-default := '(' <key>, <value> ')'
      key := (<item-index> | <item-name>)
      value := <default-value>

.. index::
   pair: parameters; module

.. _param_module:

module
''''''
Sets '*__module__*' of the created class definition.
Available beginning with *Python-3.6*.

See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.


.. index::
   pair: parameters; rename

.. _param_rename:

rename
''''''
If *True* replaces silently invalid field names by
'*_<item-index>*'.
Available beginning with *Python-2.7*, in *Python3* beginning with  *Python-3.1* - so not in *Python-3.0*.

See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.


.. index::
   pair: parameters; typename

.. _param_typename:

typename
''''''''
Name of returned class of type *namedtuple*.
The actual registered top-level base class is *namedtupledefsABC* - underneath *object* of course.

See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.


.. index::
   pair: parameters; verbose

.. _param_verbose:

verbose
'''''''
Prints created class definition.

See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.




The call interface provides for groups of functions and classes with a set of 
common parameters and additional context specific modifications.

The provided function sets comprise the categories:

* Filesystem Positions and Navigation

* Canonical Node Address

Various common options are supported, which may not be available for each interface.

.. _RETURN_namedtuple:

Created Named Tuple Class
^^^^^^^^^^^^^^^^^^^^^^^^^
The created named tuple class is extended by the default values *fielddefaults*,
which is coverd by the creation interface.

In addition the method ":ref:`_merge <DYNAMICCREATEDNAMEDTUPLE>`" is added
to the template, which supports the type-accurate merge of named tuples.
The standard *collections.tuple* returns for the addition(merge) of named tuples
the base class *tuple*, while the *namedtupledef.namedtuple* returns a new instance
of merged classes as a named tuple including combined default values.
 

.. _namedtupledefs_REFERENCES:

Resources
---------

* [namedtuple]_ namedtuple - The Python Standard Library - lib/collections
* [PYFUNC]_ The Python Language Reference - Function definitions


.. |bs| raw:: html

   <code>&#92;</code>

.. |dbs| raw:: html

   <code>&#92;&#92;</code>
   