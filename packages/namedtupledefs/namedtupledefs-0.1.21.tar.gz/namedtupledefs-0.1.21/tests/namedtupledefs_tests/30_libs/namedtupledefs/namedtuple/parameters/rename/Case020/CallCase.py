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

        resx = ('_0', '_1', '_2')
        res = namedtuple('MyClassABC', ('!f0', '_f1', '%f2'),
                         rename=True, 
#                         verbose=True,
                         fielddefaults=(22,33,)
                         )
        
        res_name = res.__name__
        self.assertEqual(res_name, 'MyClassABC')
        
        res_base_name = res.__class__.__name__
        self.assertEqual(res_base_name, 'type')

        res_fields = res._fields
        self.assertEqual(res_fields, ('_0', '_1', '_2'))

        self.assertTrue(isinstance(res, type))

        self.assertTrue(res, resx)
        
        myinst = res(11,)
        myinstx = (11, 22, 33,)
        self.assertEqual(myinst, myinstx)
        

if __name__ == '__main__':
    unittest.main()

