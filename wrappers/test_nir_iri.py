#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

# The wrapper classes to test.
from nir import NIR
from iri import IRI

class TestNIRvsIRI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nir_vs_iri(self):

        ## The subject ID.
        subject_id = "000000_00_00_00"

        ## The NIR test CSV file.
        nir = NIR("testdata/NIR/%s.csv" % (subject_id))

        ## The IRI test CSV file.
        iri = IRI("testdata/IRI/%s.csv" % (subject_id))

        # The tests.

        # Check the total number of outer rings found in the NIR file matches
        # the number of blobs found in the IRI file.
        self.assertEqual(sum(nir.get_number_of_inner_rings_data()), iri.get_number_of_entries())


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_nir_to_iri.log', filemode='w', level=lg.DEBUG)

    lg.info(" *")
    lg.info(" *================================================")
    lg.info(" * Logger output from wrappers/test_nir_to_iri.py ")
    lg.info(" *================================================")
    lg.info(" *")

    unittest.main()
