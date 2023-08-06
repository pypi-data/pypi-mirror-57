
.. _API_namedtupledefs_init:

namedtupledefs.__init__
***********************


Module
------

.. automodule:: namedtupledefs.__init__

Functions
---------

.. _API_namedtuple:

namedtuple
^^^^^^^^^^
.. autofunction:: namedtuple

Args:

   .. index::
      pair: parameters; typename
   
   **typename**:

      Name of returned class of type *namedtuple*.
      The actual registered top-level base class is *namedtupledefsABC* - underneath *object* of course.
      
      See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.
      
   .. index::
      pair: parameters; fieldnames
      pair: parameters; _fieldnames
   
   **field_names**:

      Symbolic names of fields with identical semantics as the standard library *collections.namedtuple*.
      When used in combination with the parameter *fielddefaults* the semantics changes to the behaviour
      of function parameters with default values, see [PYFUNC]_.  
      
         .. parsed-literal::
      
            field_names := (
                 <field-name>
               | <fieldnames>
            )
   
            fieldnames := '(' <field-name> [, <fieldnames>] ')'
            field-name := <valid-character-one>[<field-name-tail>] 
            field-name-tail := <valid-character>[<field-name-tail>]
            valid-character-one := [a-zA-Z] 
            valid-character := [a-zA-Z_0-9] 
      
      See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.
            
       
   .. index::
      pair: parameters; module
   
   **module**

      Sets '*__module__*' of the created class definition.
      Available beginning with *Python-3.6*.
      
      See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.
   
   .. index::
      pair: parameters; rename
   
   **rename**

      If *True* replaces silently invalid field names by
      '*_<item-index>*'.
      Available beginning with *Python-2.7*, in *Python3* beginning with  *Python-3.1* - so not in *Python-3.0*.
      
      See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.


   .. index::
      pair: parameters; verbose
   
   **verbose**

      Prints created class definition.
      
      See also `usage of parameters <genindex.html#P>`_, and [namedtuple]_.
   

   kargs:
   
      .. index::
         pair: parameters; _fielddefaults
         pair: parameters; fielddefaults
      
      **fielddefaults**
   
      Optional support for default values of *fieldnames*.
      A list of values.
      Same semantics as the function call interfaces [PYFUNC]_,
      
         .. parsed-literal::
      
            fielddefaults := '(' <item-default> [, <fielddefaults>] ')'
            item-default := '(' <key>, <value> ')'
            key := (<item-index> | <item-name>)
            value := <default-value>
   

Returns:
   A named tuple class.

Raises:
   TypeError
   
   ValueError
   
   SyntaxError

Classes
-------

.. _DYNAMICCREATEDNAMEDTUPLE:

**Dynamic Created namedtuple**

The factory function creates a dynamic class by the compilation of the following string.
This is performed for each created *namedtuple*.

.. _CODE_PYTHON2:

Class Template Python2
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   :linenos:

   from builtins import property as _property, tuple as _tuple
   from operator import itemgetter as _itemgetter
   from collections import OrderedDict
   
   import namedtupledefs
   
   class {typename}(tuple):
       '''{typename}({arg_list}) 
       with optional default values fielddefaults={field_defaults} => {typename}({new_args})'''
   
       __slots__ = ()
   
       _fields = {field_names!r}
       _fielddefaults = {field_defaults}
   
       def __new__(_cls, {new_args}):
           'Create new instance of {typename}({new_args})'
           return _tuple.__new__(_cls, ({arg_list}))
   
       @classmethod
       def _make(cls, iterable, new=tuple.__new__, len=len):
           'Make a new {typename} object from a sequence or iterable'
           result = new(cls, iterable)
           if len(result) != {num_fields:d}:
               raise TypeError('Expected {num_fields:d} arguments, got %d' % len(result))
           return result
   
       def _replace(_self, **kwds):
           'Return a new {typename} object replacing specified fields with new values'
           result = _self._make(map(kwds.pop, {field_names!r}, _self))
           if kwds:
               raise ValueError('Got unexpected field names: %r' % list(kwds))
           return result
   
       def __repr__(self):
           'Return a nicely formatted representation string'
           return self.__class__.__name__ + '({repr_fmt})' % self
   
       def _asdict(self):
           'Return a new OrderedDict which maps field names to their values.'
           return OrderedDict(zip(self._fields, self))
   
       def __getnewargs__(self):
           'Return self as a plain tuple.  Used by copy and pickle.'
           return tuple(self)
   
       __dict__ = _property(_asdict)
   
       def __getstate__(self):
           'Exclude the OrderedDict from pickling'
           pass
   
       def _merge(self, typename, *others):
           'Add multiple "namedtuple" resulting in a new "namedtuple" of class "typename".'
           _fn = copy(self._fields)
           _fd = copy(self._fielddefaults)  # spare None-check
           _t = ()
           for o in others:
               if not hasattr(o, '_fields') or not hasattr(o, '_fielddefaults'):
                   raise ValueError(
                       "supports only classes from: namedtupledefs.namedtuple " + str(o))
               # check for non-scattered function style default values
               if _fd and (not o._fielddefaults or len(o._fielddefaults) != len(o._fields)):
                   raise ValueError(
                       "default values are right bound and must not be scattered: %s / %s"
                       %(str(o._fields), str(o._fielddefaults))
                       )
               _fn += o._fields
               _fd += o._fielddefaults
               _t  += o  # want the tuple values without fiddling
           # resulting names have to be valid - the tuple will check finally 
           tp = namedtupledefs.namedtuple(typename, _fn, fielddefaults=_fd)
           return tp(*tuple.__add__(self, _t))
   
   {field_defs}


.. _CODE_PYTHON3:

Class Template Python3
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   :linenos:

   from builtins import property as _property, tuple as _tuple
   from operator import itemgetter as _itemgetter
   from collections import OrderedDict
   
   import namedtupledefs
   
   class {typename}(tuple):
       '''{typename}({arg_list}) 
       with optional default values fielddefaults={field_defaults} => {typename}({new_args})'''
   
       __slots__ = ()
   
       _fields = {field_names!r}
       _fielddefaults = {field_defaults}
   
       def __new__(_cls, {new_args}):
           'Create new instance of {typename}({new_args})'
           return _tuple.__new__(_cls, ({arg_list}))
   
       @classmethod
       def _make(cls, iterable, new=tuple.__new__, len=len):
           'Make a new {typename} object from a sequence or iterable'
           result = new(cls, iterable)
           if len(result) != {num_fields:d}:
               raise TypeError('Expected {num_fields:d} arguments, got %d' % len(result))
           return result
   
       def _replace(_self, **kwds):
           'Return a new {typename} object replacing specified fields with new values'
           result = _self._make(map(kwds.pop, {field_names!r}, _self))
           if kwds:
               raise ValueError('Got unexpected field names: %r' % list(kwds))
           return result
   
       def __repr__(self):
           'Return a nicely formatted representation string'
           return self.__class__.__name__ + '({repr_fmt})' % self
   
       def _asdict(self):
           'Return a new OrderedDict which maps field names to their values.'
           return OrderedDict(zip(self._fields, self))
   
       def __getnewargs__(self):
           'Return self as a plain tuple.  Used by copy and pickle. Does not need the fielddefaults.'
           return tuple(self)
   
       __dict__ = _property(_asdict)
   
       def __getstate__(self):
           'Exclude the OrderedDict from pickling'
           pass
   
       def _merge(self, typename, *others):
           'Add multiple "namedtuple" resulting in a new "namedtuple" of class "typename".'
           _fn = copy(self._fields)
           _fd = copy(self._fielddefaults)  # spare None-check
           _t = ()
           for o in others:
               if not hasattr(o, '_fields') or not hasattr(o, '_fielddefaults'):
                   raise ValueError(
                       "supports only classes from: namedtupledefs.namedtuple " + str(o))
               # check for non-scattered function style default values
               if _fd and (not o._fielddefaults or len(o._fielddefaults) != len(o._fields)):
                   raise ValueError(
                       "default values are right bound and must not be scattered: %s / %s"
                       %(str(o._fields), str(o._fielddefaults))
                       )
               _fn += o._fields
               _fd += o._fielddefaults
               _t  += o  # want the tuple values without fiddling
           # resulting names have to be valid - the tuple will check finally 
           tp = namedtupledefs.namedtuple(typename, _fn, fielddefaults=_fd)
           return tp(*tuple.__add__(self, _t))
   
   {field_defs}


Changed Interfaces
^^^^^^^^^^^^^^^^^^
The following interfaces were changed from the sources of *collections.namedtuple*.

.. _API_NEW:

**__new__**
   The parameterlist is changed from *{arg_list}* to *{new_args}*,
   which is generated with default values.

New Interfaces
^^^^^^^^^^^^^^

.. _API_MERGE:

**_merge**
   The method merge is introduced.
   The method provides the addition of multiple *namedtuple* into a new *namedtuple*
   with a provided class name.
   This includes the concatenation of the fieldnames as well as the appropriate
   handling of the *fielddefaults*.
   
   Args:
      **typename**:
         The name of the merged class.
         
      **others**:
         The list of instances to be merged.
   
   Returns:
      A created new *namedtuple* object with merged *data*, *_fields*, and *fielddefaults*.
      
   Raises:
      ValueError
    
   Example:
   
      .. code-block:: python
         :linenos:
        
         A = namedtuple('TestClass', ('a', 'b', 'c'), fielddefaults=(22, 33))
         B = namedtuple('TestClass1', ('d', ), fielddefaults=(44,))
         C = namedtuple('TestClass2', ('e', 'f',), fielddefaults=(55, 66,))
         
         t0 = A(11,)
         self.assertEqual(t0, (11, 22, 33))
         
         t1 = B()
         self.assertEqual(t1, (44,))
         
         t2 = C()
         self.assertEqual(t2, (55, 66,))
         
         tx = t0._merge('TestClassSum', t1, t2)
         self.assertEqual(tx, (11, 22, 33, 44, 55, 66,))

Remarks
^^^^^^^

.. _API_MAKE:

**_make**

   The *_make* class method creates a new object from the current class.
   This includes the *_fielddefaults*.
   The call could be applied by using default values.
   
      .. code-block:: python
         :linenos:
        
         A = namedtuple('TestClass', ('a', 'b', 'c'), fielddefaults=(333, 444,))
         
         t = A(1,)
         a = A._make(t)
         print(a)
         
         self.assertEqual(a, (1, 333, 444))
      

Exceptions
----------

.. raw:: html

   </div>
   </div>

Uses standard exceptions:

* *SyntaxError*
* *TypeError*
* *ValueError*


