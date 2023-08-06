
.. _NAMEDTUPLEDEFS_NAMEDTUPLE:

namedtupledefs.namedtuple
=========================
Provides drop-in-replacement without the use of the optional default values.
See docstring.

::

   >>> Point = namedtuple('Point', ['x', 'y', 'z'])
   >>> Point.__doc__                   # docstring for the new class with defaults
   'Point(x, y, z)\n    with optional default values fielddefaults=()'
   >>> Point(11, 22, 33)               # instantiate with partial positional args or keywords
   Point(x=11, y=22, z=33)
