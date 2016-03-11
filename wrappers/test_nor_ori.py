#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper classes to test.
from nor import NOR
from ori import ORI

class TestNORvsORI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nor_vs_ori(self):

        ## The subject ID.
        subject_id = "000000_00_00_00"

        ## The NOR test CSV file.
        nor = NOR("testdata/NOR/%s.csv" % (subject_id))

        ## The ORI test CSV file.
        ori = ORI("testdata/ORI/%s.csv" % (subject_id))

        # The tests.

        # Check the total number of outer rings found in the NOR file matches
        # the number of blobs found in the ORI file.
        self.assertEqual(sum(nor.get_number_of_outer_rings_data()), ori.get_number_of_entries())


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_nor_to_ori.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *================================================")
    lg.info(" * Logger output from wrappers/test_nor_to_ori.py ")
    lg.info(" *================================================")
    lg.info(" *")

    unittest.main()
