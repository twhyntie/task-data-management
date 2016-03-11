#!/usr/bin/env python

# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from nod import NOD

class TestNOD(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nod(self):

        ## The annotation CSV file.
        nod = NOD("testdata/NOD/000000_00_00_00.csv")

        # The tests.

        # The headers.
        self.assertEqual(nod.get_number_of_headers(), 2)
        self.assertEqual(nod.get_header(0), "annotation_id")
        self.assertEqual(nod.get_header(1), "n_oddities_identified")

        # The annotations.

        # Test the number of annotations found.
        self.assertEqual(nod.get_number_of_annotations(), 88)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_nod.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_nod.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
