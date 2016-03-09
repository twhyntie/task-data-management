#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The SCL wrapper class to test.
from spl import SPL

class TestSPL(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_scl(self):

        ## The SPL test image.
        spl = SPL("testdata/SPL/000000_00_00_00.png")

        # The tests.

        # The size of the image.
        self.assertEqual(spl.get_image_width(),  65)
        self.assertEqual(spl.get_image_height(), 65)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_spl.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_spl.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
