#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

# The CSV file wrapper class.
from csvfile import CSVFile

class BLB(CSVFile):
    """
    Wrapper class for the blob information CSV file format.
    """
    def __init__(self, path):
        """ Constructor. """
        super(BLB, self).__init__(path)

        ## A dictionary for the data.
        #
        # { annotation ID:data }
        self.__data_dict = {}

#        # Extract the data from the CSV data.
#        for line in self.get_data():
#            vals = line.strip().split(",")
#            if vals[0] not in self.__data_dict.keys():
#                self.__data_dict[vals[0]] = int(vals[1])

    def get_number_of_blobs(self):
        return self.get_number_of_entries()
