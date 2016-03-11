#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper class to test.
from iri import IRI

class TestIRI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_iri(self):

        ## The IRI annotation CSV file.
        iri = IRI("testdata/IRI/000000_00_00_00.csv")

        # The tests.

        # The headers.
        self.assertEqual(iri.get_number_of_headers(), 4)
        self.assertEqual(iri.get_header(0), "annotation_id")
        self.assertEqual(iri.get_header(1), "x")
        self.assertEqual(iri.get_header(2), "y")
        self.assertEqual(iri.get_header(3), "r")

        # The annotations.

        # Test the number of inner rings found.
        self.assertEqual(iri.get_number_of_inner_rings(), 211)


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_iri.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *=========================================")
    lg.info(" * Logger output from wrappers/test_iri.py ")
    lg.info(" *=========================================")
    lg.info(" *")

    unittest.main()
