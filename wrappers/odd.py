#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

# The CSV file wrapper class.
from csvfile import CSVFile

class ODD(CSVFile):
    """
    Wrapper class for the oddity information CSV file format.
    """
    def __init__(self, path):
        """ Constructor. """
        super(ODD, self).__init__(path)

        ## A dictionary for the data.
        #
        # { annotation ID:data }
        self.__data_dict = {}

    def get_number_of_oddities(self):
        return self.get_number_of_entries()
