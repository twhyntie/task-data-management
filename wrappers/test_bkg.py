#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from bkg import BKG

class TestBKG(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bkg(self):

        ## The BKG annotation CSV file.
        bkg = BKG("testdata/BKG/000000_00_00_00.csv")

        # The tests.

        # The headers.
        self.assertEqual(bkg.get_number_of_headers(), 2)
        self.assertEqual(bkg.get_header(0), "annotation_id")
        self.assertEqual(bkg.get_header(1), "background_assessment")

        # The annotations.

        # Test the number of blobs found.
        self.assertEqual(bkg.get_number_of_background_assessments(), 88)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_bkg.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_bkg.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
