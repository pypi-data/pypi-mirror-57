from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

_myglobal = 1

import unittest

import os
from namedtupledefs import namedtuple
import pickle

MyClass = namedtuple(
            'MyClass', 
            ('f0', 'f1', 'f2',), 
            fielddefaults=(11, 22, 33,),
            rename=True,
#            module='/my/module',
#            verbose=True,
          )

class CallUnits(unittest.TestCase):

    def testCase000(self):


        myinstance = MyClass(1, 2, 3)
        self.assertEqual(myinstance, (1, 2, 3))
        
        _myfile = os.path.dirname(__file__) + os.sep + 'test.p'
        f = open(_myfile, 'wb')
        pickle.dump(myinstance, f, protocol=2)
        f.close()
        
        f = open(_myfile, 'rb')
        myinstance_copy = pickle.load(f)
        f.close()

        self.assertEqual(myinstance, myinstance_copy)
        
if __name__ == '__main__':
    unittest.main()

