#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the OS stuff.
import os

#...for the logging.
import logging as lg

#...for the plotting.
import matplotlib.pyplot as plt

#...for the MATH.
import numpy as np

# Load the LaTeX text plot libraries.
from matplotlib import rc

# Uncomment to use LaTeX for the plot text.
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)

class FrequencyHistogram:

    def __init__(self, data, plot_filename, **kwargs):

        lg.info(" * Initialising frequency histogram.")
        lg.info(" *")

        ## The figure upon which to display the scan image.
        plot = plt.figure(102, figsize=(5.0, 5.0), dpi=150, facecolor='w', edgecolor='w')

        # Adjust the position of the axes.
        plot.subplots_adjust(bottom=0.17, left=0.15)

        ## The plot axes.
        plotax = plot.add_subplot(111)

        ## The name of the object being counted.
        self.__object_name = "object"
        if "object_name" in kwargs.keys():
            self.__object_name = kwargs["object_name"]

        # Set the x axis label.
        if "x_label" in kwargs.keys():
            plt.xlabel("%s" % (kwargs["x_label"]))
        else:
            plt.xlabel("Number of %ss identified" % (self.__object_name))

        # Set the y axis label.
        plt.ylabel("Number of classifications")

        # A list of bin edges.
        my_bins = range(max(data)+2)

        # Make the histogram.
        n, bins, patches = plt.hist(data, bins=my_bins, histtype='stepfilled', align='left')

        # Set the plot's visual properties.
        plt.setp(patches, 'facecolor', 'g', 'alpha', 0.75, 'linewidth', 0.0)

        ## An array for the x axis tick values.
        x_ticks = np.arange(0, max(data)+2)

        # Set the x axis ticks accordingly.
        plotax.set_xticks(x_ticks)

        # Set the x axis limits to make sure the whole bar width is displayed.
        plotax.set_xlim([-0.5, max(data)+0.5])

        # Add a grid.
        plt.grid(1)

        # Save the figure.
        plot.savefig(plot_filename)

        print("* Created: '%s - %d classifications." % (plot_filename, len(data)))

        plot.clf()
