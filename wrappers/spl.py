#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

#...for the image manipulation.
import matplotlib.image as mpimg

class SPL:
    """
    Wrapper class for the split TASL scan images.
    """

    def __init__(self, image_path):
        """ Constructor. """

        ## The image filename (including path).
        self.__image_path = image_path

        # Load in the image.

        ## The image as a NumPy array.
        self.__img = mpimg.imread(self.__image_path)

        ## The image dimensions.

        lg.debug("* Initialising SPL object from '%s'." % (self.__image_path))
        lg.debug("* Image dimensions: %s" % (str(self.__img.shape)))

        lg.debug("*")

    def get_filename(self):
        return self.__filename
    def get_image_width(self):
        return self.__img.shape[0]
    def get_image_height(self):
        return self.__img.shape[1]
