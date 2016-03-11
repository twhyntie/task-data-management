#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

# The CSV file wrapper class.
from csvfile import CSVFile

# For the frequency histogram.
from plotting import FrequencyHistogram

class BKG(CSVFile):
    """
    Wrapper class for the background assessment information CSV file format.
    """
    def __init__(self, path):
        """ Constructor. """
        super(BKG, self).__init__(path)

        ## A dictionary for the data.
        #
        # { annotation ID:data }
        self.__data_dict = {}

    def get_number_of_background_assessments(self):
        return self.get_number_of_entries()

    def make_frequency_histogram(self, path):

        # Convert the background assessment information into a usable list.

        assessments = []

        # Get the data.

        for i, row in enumerate(self.get_data()):

            # The annotation ID.
            anno_id = row.strip().split(",")[0]

            # The assessment from the annotation.
            assessment = row.strip().split(",")[1]

            if "Pretty empty" in assessment:
                assessments.append(0)
            elif "few wiggles" in assessment:
                assessments.append(1)
            elif "Fairly wiggly" in assessment:
                assessments.append(2)
            elif "Very wiggly" in assessment:
                assessments.append(3)
            elif "a mess" in assessment:
                assessments.append(4)

        ## The frequency histogram.
        self.__fh = FrequencyHistogram(assessments, path, x_label="Background assessment")
