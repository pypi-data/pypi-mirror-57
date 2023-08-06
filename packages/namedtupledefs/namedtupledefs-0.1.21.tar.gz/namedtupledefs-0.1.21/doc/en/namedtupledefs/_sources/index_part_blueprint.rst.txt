
Blueprint
=========

.. _REFERENCE_ARCHITECTURE:

The package 'namedtupledefs' provides a patched version of the *collections.namedtuple* 
with field defaults for *namedtuple*. This is a drop-in compatible patch with minimal
changes only - basically one line in the class template only. 

Just use:

   .. parsed-literal::

      import namedtupledefs
      
      Point0 = namedtupledefs.namedtuple('Point', ('x', 'y', 'z'))
      Point1 = namedtupledefs.namedtuple('Point', ('x y z'))
      
      point0 = Point0(11, 22, 33) 
      point1 = Point1(11, 22, 33) 

the same with defaults:

   .. parsed-literal::

      from namedtupledefs import namedtuple
      
      Point0defs = namedtupledefs.namedtuple('Point0', ('x', 'y', 'z'), fielddefaults=(22, 33))
      Point1defs = namedtupledefs.namedtuple('Point1', ('x y z'), fielddefaults=(22, 33))
      
      point0defs = Point0(11, 22) 
      point1defs = Point1(11) 

with the identical results:
   
   .. parsed-literal::

      point0defs == point0 
      point1defs == point1 

of the printout:

   .. parsed-literal::

      >>> point0
      Point0(x=11, y=22, z=33)
      
      >>> point0defs
      Point0(x=11, y=22, z=33)

      >>> point1
      Point1(x=11, y=22, z=33)
      
      >>> point1defs
      Point1(x=11, y=22, z=33)

For merging multiple *namedtuple* results into one of type named tuple:

   .. parsed-literal::

      >>> point0
      Point0(a=11, b=22, c=33)
      
      >>> point1
      Point1(d=44, e=55)
      
      >>> point2
      Point1(f=66)

      >>> psum = point0._merge('PointSum', point1, point2)
      PointSum(a=11, b=22, c=33, d=44, e=55, f=66)

The next example shows the assembly of a *URL* which is processed into seperate parts,
and finally concatenated into one named tuple.

   .. parsed-literal::

      # example: RFC3986 - 3. Syntax Components
      Scheme = namedtuple('Scheme', ('scheme',), fielddefaults=('https',), verbose=True)
      HierPart = namedtuple('HierPart', ('authority', 'path'), fielddefaults=('', '/'))
      Query = namedtuple('Query', ('name', ), fielddefaults=('ferret',))
      Fragment = namedtuple('Fragment', ('f0', ), fielddefaults=('nose',))
      
      
      scheme = Scheme()
      self.assertEqual(scheme, ('https',))
      
      hier_part = HierPart('example.com:8042', '/over/there', )
      self.assertEqual(hier_part, ('example.com:8042', '/over/there', ))
      
      query = Query('ferret',)
      self.assertEqual(query, ('ferret',))
      
      fragment = Fragment()
      self.assertEqual(fragment, ('nose',))
      
      url = scheme._merge('MyURI', hier_part, query, fragment)
      self.assertEqual(
         url, 
         ('https', 'example.com:8042', '/over/there', 'ferret', 'nose',)
      )
      self.assertEqual(url.__class__.__name__, 'MyURI')
 
See doc-string for more examples.

The contained interfaces are:

- **namedtupledefs.namedtuple**:
   
  The drop-in replacement of *collections.namedtuple* with optional default values.

For the standard library *collections.namedtuple* see Python documentation [namedtuple]_.
