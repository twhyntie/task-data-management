#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper classes to test.
from nbl import NBL
from blb import BLB

class TestNBLvsBLB(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nbl_vs_blb(self):

        ## The subject ID.
        subject_id = "000000_00_00_00"

        ## The NBL test CSV file.
        nbl = NBL("testdata/NBL/%s.csv" % (subject_id))

        ## The BLB test CSV file.
        blb = BLB("testdata/BLB/%s.csv" % (subject_id))

        # The tests.

        # Check the total number of blobs found in the NBL file matches the
        # number of blobs found in the BLB file.
        self.assertEqual(sum(nbl.get_number_of_blobs_data()), blb.get_number_of_entries())


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_nbl_to_blb.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *================================================")
    lg.info(" * Logger output from wrappers/test_nbl_to_blb.py ")
    lg.info(" *================================================")
    lg.info(" *")

    unittest.main()
