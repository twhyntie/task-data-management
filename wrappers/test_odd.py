#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from odd import ODD

class TestODD(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_odd(self):

        ## The ODD annotation CSV file.
        odd = ODD("testdata/ODD/000000_00_00_00.csv")

        # The tests.

        # The headers.
        self.assertEqual(odd.get_number_of_headers(), 3)
        self.assertEqual(odd.get_header(0), "annotation_id")
        self.assertEqual(odd.get_header(1), "x")
        self.assertEqual(odd.get_header(2), "y")

        # The annotations.

        # Test the number of blobs found.
        self.assertEqual(odd.get_number_of_oddities(), 74)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_odd.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_odd.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
