#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The SCL wrapper class to test.
from scl import SCL

class TestSCL(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_scl(self):

        ## The SCL test image.
        scl = SCL("testdata/SCL/000000_00_00_00.png")

        # The tests.

        # The size of the image.
        self.assertEqual(scl.get_image_width(),  390)
        self.assertEqual(scl.get_image_height(), 390)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_scl.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_scl.py ")
    lg.info(" * =========================================")
    lg.info(" *")

    unittest.main()
