#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

# The CSV file wrapper class.
from csvfile import CSVFile

# For the frequency histogram.
from plotting import FrequencyHistogram

class NIR(CSVFile):
    """
    Wrapper class for the "Number of outer rings identified" CSV file format.
    """
    def __init__(self, path):
        """ Constructor. """
        super(NIR, self).__init__(path)

        ## A dictionary for the data.
        #
        # { annotation ID:data }
        self.__data_dict = {}

        # Extract the data from the CSV data.
        for line in self.get_data():
            vals = line.strip().split(",")
            if vals[0] not in self.__data_dict.keys():
                self.__data_dict[vals[0]] = int(vals[1])

    def get_number_of_annotations(self):
        return self.get_number_of_entries()

    def get_number_of_inner_rings_data(self):
        return self.__data_dict.values()

    def make_frequency_histogram(self, path):
        self.__fh = FrequencyHistogram(self.__data_dict.values(), path, object_name='inner ring')
