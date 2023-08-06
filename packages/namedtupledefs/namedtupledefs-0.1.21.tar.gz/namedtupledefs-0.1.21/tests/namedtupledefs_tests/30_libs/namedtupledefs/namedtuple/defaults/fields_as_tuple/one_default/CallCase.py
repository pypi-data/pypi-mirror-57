from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "19683f50-48f2-4e1e-953f-640455e97340"

__docformat__ = "restructuredtext en"

import unittest

import namedtupledefs

class CallUnits(unittest.TestCase):

    def testCase000(self):

        resx = (11, 22, 33)

        Point = namedtupledefs.namedtuple('MyClassABC', ('x', 'y', 'z'), fielddefaults=(33,))
        point = Point(11, 22)

        res = (point.x, point[1], point.z)
        
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()

