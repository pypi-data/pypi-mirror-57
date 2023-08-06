from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest
from pythonids import PYV31, PYV3, PYVxyz

from namedtupledefs import namedtuple

class CallUnits(unittest.TestCase):

    def testCase000(self):
        if PYVxyz > PYV31 or PYVxyz < PYV3:
            pass
        else:
            self.skipTest("requires >=3.1 or <3")

        # example: RFC3986 - 3. Syntax Components
        Scheme = namedtuple('Scheme', ('scheme',), fielddefaults=('https',),)
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
        
        

if __name__ == '__main__':
    unittest.main()

