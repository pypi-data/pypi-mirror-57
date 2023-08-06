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

from yapydata.datatree.synjson4627 import DataTreeJSON4627, YapyDataJSON4627Error


class CallUnits(unittest.TestCase):
    def testCase010(self):
        self.assertRaises(YapyDataJSON4627Error, DataTreeJSON4627, 123.11)


if __name__ == '__main__':
    unittest.main()
