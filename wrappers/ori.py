#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

# The CSV file wrapper class.
from csvfile import CSVFile

class ORI(CSVFile):
    """
    Wrapper class for the outer ring information CSV file format.

    Each entry (row) in the file corresponds to one outer ring
    identified by a given volunteer in a given classification.
    """
    def __init__(self, path):
        """ Constructor. """
        super(ORI, self).__init__(path)

        ## A dictionary for the data.
        #
        # { annotation ID:data }
        self.__data_dict = {}

    def get_number_of_outer_rings(self):
        return self.get_number_of_entries()
