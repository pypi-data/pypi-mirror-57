from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"

import unittest
import os
import sys

from yapydata.datatree.synjson import DataTreeJSON



class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
 #       sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        _cap = DataTreeJSON(
            {
                'a': {
                    'b': [
                        {
                            'c': [
                                123,
                                456,
                            ]
                        }
                    ]
                } 
            }
        )
        resx = {
                'a': {
                    'b': [
                        {
                            'c': [
                                123,
                                456,
                                789,
                            ]
                        }
                    ]
                } 
            }

        _cap.create('a', 'b', 0, 'c', 2, value=789)
        self.assertEqual(_cap.data, resx)


if __name__ == '__main__':
    unittest.main()
