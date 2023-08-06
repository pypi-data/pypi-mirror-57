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


#         A = namedtuple('TestClass', ('a', 'b', 'c'), verbose=True, fielddefaults=(22, 33))
#         B = namedtuple('TestClass1', ('d', ), verbose=True, fielddefaults=(44,))
#         C = namedtuple('TestClass2', ('e', 'f',), verbose=True, fielddefaults=(55, 66,))
 
        A = namedtuple('TestClass', ('a', 'b', 'c'), fielddefaults=(22, 33))
        B = namedtuple('TestClass1', ('d', ), fielddefaults=(44,))
        C = namedtuple('TestClass2', ('e', 'f',), fielddefaults=(55, 66,))

        t0 = A(11, 22, 33)
        self.assertEqual(t0, (11, 22, 33))
        
        t1 = A(11, 22, )
        self.assertEqual(t1, (11, 22, 33))
        
        t2 = A(33,)
        self.assertEqual(t2, (33, 22, 33))
        
        t3 = B()
        self.assertEqual(t3, (44,))
        
        t4 = C(55,66,)
        self.assertEqual(t4, (55, 66,))
        
        tx = t1._merge('TestClassSum', t3, t4)
        self.assertEqual(tx, (11, 22, 33, 44, 55, 66,))
        

if __name__ == '__main__':
    unittest.main()

