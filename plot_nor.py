#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 MoEDAL and CERN@school - Plotting NOR information.

 See the README.md file and the GitHub wiki for more information.

 http://cernatschool.web.cern.ch

"""

# Import the code needed to manage files.
import os, glob

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

# The NOR wrapper class.
from wrappers.nor import NOR

if __name__ == "__main__":

    print("*")
    print("*==================================================*")
    print("* MoEDAL and CERN@school: Plotting NOR information *")
    print("*==================================================*")
    print("*")

    # Get the datafile path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("dataPath",       help="Path to the input dataset.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The root data path.
    data_path = args.dataPath

    # Check if the input file exists. If it doesn't, quit.
    if not os.path.exists(data_path):
        raise IOError("* ERROR: '%s' input file does not exist!" % (data_path))

    ## The number of outer rings data path.
    nor_path = os.path.join(data_path, "NOR")
    if not os.path.isdir(nor_path):
        raise IOError("* ERROR: '%s' does not exist - no input data!" % (nor_path))

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('./.', 'log_plot_nor.log'), filemode='w', level=level)

    lg.info(" *")
    lg.info(" *==================================================*")
    lg.info(" * MoEDAL and CERN@school: Plotting NOR information *")
    lg.info(" *==================================================*")
    lg.info(" *")
    lg.info(" * Plotting number of outer rings information in : '%s'" % (nor_path))
    lg.info(" *")

    # Loop over the found outer ring information.
    for i, nor_csv_path in enumerate(sorted(glob.glob(os.path.join(nor_path, "*.csv")))):

        ## The subject ID.
        sub_id = os.path.basename(nor_csv_path)[:-4]

        ## The NOR wrapper object.
        nor = NOR(nor_csv_path)

        ## The path of the plot image.
        nor_plot_image_path = os.path.join(nor_path, "%s.png" % (sub_id))

        # Make the plot.
        nor.make_frequency_histogram(nor_plot_image_path)
