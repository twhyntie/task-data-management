#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from ori import ORI

class TestORI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ori(self):

        ## The ORI annotation CSV file.
        ori = ORI("testdata/ORI/000000_00_00_00.csv")

        # The tests.

        # The headers.
        self.assertEqual(ori.get_number_of_headers(), 4)
        self.assertEqual(ori.get_header(0), "annotation_id")
        self.assertEqual(ori.get_header(1), "x")
        self.assertEqual(ori.get_header(2), "y")
        self.assertEqual(ori.get_header(3), "r")

        # The annotations.

        # Test the number of outer rings found.
        self.assertEqual(ori.get_number_of_outer_rings(), 236)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_ori.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_ori.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
