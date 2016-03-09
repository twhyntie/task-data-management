#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from nbl import NBL

class TestNBL(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nbl(self):

        ## The NBL annotation CSV file.
        nbl = NBL("testdata/NBL/000000_00_00_00.csv")

        # The tests.

        # The headers.
        self.assertEqual(nbl.get_number_of_headers(), 2)
        self.assertEqual(nbl.get_header(0), "annotation_id")
        self.assertEqual(nbl.get_header(1), "n_blobs_identified")

        # The annotations.

        # Test the number of annotations found.
        self.assertEqual(nbl.get_number_of_annotations(), 88)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_nbl.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_nbl.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
