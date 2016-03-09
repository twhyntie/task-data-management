#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper classes to test.
from spl import SPL
from scl import SCL

class TestSPLtoSCL(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_spl_to_scl(self):

        ## The subject ID.
        subject_id = "000000_00_00_00"

        ## The SPL test image.
        spl = SPL("testdata/SPL/%s.png" % (subject_id))

        ## The SCL test image.
        scl = SCL("testdata/SCL/%s.png" % (subject_id))

        # The tests.

        ## The scale factor.
        scale_factor = 6.0

        # Check the image has been scaled properly (i.e. by the scale factor).
        self.assertEqual(scl.get_image_width(),  spl.get_image_width()  * scale_factor)
        self.assertEqual(scl.get_image_height(), spl.get_image_height() * scale_factor)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_spl_to_scl.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *================================================")
    lg.info(" * Logger output from wrappers/test_spl_to_scl.py ")
    lg.info(" *================================================")
    lg.info(" *")

    unittest.main()
