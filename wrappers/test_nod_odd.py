#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper classes to test.
from nod import NOD
from odd import ODD

class TestNODvsODD(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nod_vs_odd(self):

        ## The subject ID.
        subject_id = "000000_00_00_00"

        ## The NOD test CSV file.
        nod = NOD("testdata/NOD/%s.csv" % (subject_id))

        ## The ODD test CSV file.
        odd = ODD("testdata/ODD/%s.csv" % (subject_id))

        # The tests.

        # Check the total number of oddities found in the NOD file matches the
        # number of oddities found in the ODD file.
        self.assertEqual(sum(nod.get_number_of_oddities_data()), odd.get_number_of_entries())


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_nod_to_odd.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *================================================")
    lg.info(" * Logger output from wrappers/test_nod_to_odd.py ")
    lg.info(" *================================================")
    lg.info(" *")

    unittest.main()
