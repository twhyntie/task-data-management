#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

class NBL:
    """
    Wrapper class for 'number of blobs' information CSV file for a given subject.
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

        ## The annotations.
        self.__annotations = lines[1:]


    def get_path(self):
        return self.__csv_path
    def get_number_of_headers(self):
        return len(self.__headers)
    def get_header(self, column):
        return self.__headers[column]
    def get_number_of_annotations(self):
        return len(self.__annotations)
