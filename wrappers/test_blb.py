#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from blb import BLB

class TestBLB(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_blb(self):

        ## The BLB annotation CSV file.
        blb = BLB("testdata/BLB/000000_00_00_00.csv")

        # The tests.

        # The headers.
        self.assertEqual(blb.get_number_of_headers(), 4)
        self.assertEqual(blb.get_header(0), "annotation_id")
        self.assertEqual(blb.get_header(1), "x")
        self.assertEqual(blb.get_header(2), "y")
        self.assertEqual(blb.get_header(3), "r")

        # The annotations.

        # Test the number of blobs found.
        self.assertEqual(blb.get_number_of_blobs(), 188)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_blb.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_blb.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
