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

        A = namedtuple('TestClass', ('a', 'b', 'c'), fielddefaults=(22, 33))

        t0 = A(11, )
        self.assertEqual(t0, (11, 22, 33))
        
        t1 = t0._replace(a=7, b=8)
        self.assertEqual(t1, (7, 8, 33))
        

if __name__ == '__main__':
    unittest.main()

