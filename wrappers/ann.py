#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

class ANN:
    """
    Wrapper class for raw annotation CSV file for a given subject.
    """

    def __init__(self, path):
        """ Constructor. """

        ## The filename (including path).
        self.__csv_path = path

        # Read in the CSV file.
        cf = open(self.__csv_path, "r")
        lines = cf.readlines()
        cf.close()

        ## The headers (list).
        self.__headers = lines[0].strip().split(",")

        ## A dictionary of the annotations.
        #
        # {annotation_id:annotation JSON}
        self.__annotations = {}

        # Extract the annotation data from the CSV file into a dictionary.
        for line in lines[1:]:

            ## The annotation ID (user_id:timestamp}.
            anno_id = line.strip().split(",")[0]

            ## The annotation (raw JSON).
            anno = line.strip().split(",", 1)[1]

            # Add the annotation to the dictionary.
            if anno_id not in self.__annotations.keys():
                self.__annotations[anno_id] = anno
            else:
                raise IOError("* ERROR: non-unique annotation ID found!")

    def get_path(self):
        return self.__csv_path
    def get_number_of_headers(self):
        return len(self.__headers)
    def get_header(self, column):
        return self.__headers[column]
    def get_annotations(self):
        return self.__annotations
    def get_number_of_annotations(self):
        return len(self.__annotations)
