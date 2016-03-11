#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 MoEDAL and CERN@school - ANN -> ODD.

 See the README.md file and the GitHub wiki for more information.

 http://cernatschool.web.cern.ch

"""

# Import the code needed to manage files.
import os, glob

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

#...for handling the annotation JSON information.
import json

# The annotation file wrapper class.
from wrappers.ann import ANN

if __name__ == "__main__":

    print("*")
    print("*====================================*")
    print("* MoEDAL and CERN@school: ANN -> ODD *")
    print("*====================================*")
    print("*")

    # Get the datafile path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("dataPath",        help="Path to the input dataset.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The root data path.
    data_path = args.dataPath

    # Check if the input file exists. If it doesn't, quit.
    if not os.path.exists(data_path):
        raise IOError("* ERROR: '%s' input file does not exist!" % (data_path))

    ## The annotations path.
    ann_path = os.path.join(data_path, "ANN")
    if not os.path.isdir(ann_path):
        raise IOError("* ERROR: '%s' does not exist - no annotation data!" % (ann_path))

    ## The oddity information data path.
    odd_path = os.path.join(data_path, "ODD")
    if not os.path.isdir(odd_path):
        os.mkdir(odd_path)

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('./.', 'log_ann_to_odd.log'), filemode='w', level=level)

    lg.info(" *")
    lg.info(" *====================================*")
    lg.info(" * MoEDAL and CERN@school: ANN -> ODD *")
    lg.info(" *====================================*")
    lg.info(" *")
    lg.info(" * Looking for annotations in    : '%s'" % (ann_path))
    lg.info(" * Writing oddity information in : '%s'" % (odd_path))
    lg.info(" *")

    # Loop over the found annotations.
    for i, ann_csv_path in enumerate(sorted(glob.glob(os.path.join(ann_path, "*.csv")))):

        ## The subject ID.
        sub_id = os.path.basename(ann_csv_path)[:-4]

        ## The annotations found for the subject.
        annotations = ANN(ann_csv_path)

        object_list = []

        # Loop over the annotations found in the subject.
        for anno_id, anno in annotations.get_annotations().iteritems():

            ## The annotation data.
            d = json.loads(anno)

            # Loop over the task answers for this annotation.
            for entry in d:

                if entry["task"] == "T7":

                    # Get the object information from the annotation.
                    object_info = entry["value"]

                    # Add an object for each object found.
                    for object_i in object_info:
                        x = object_i["x"]
                        y = object_i["y"]
                        object_list.append("%s,%.1f,%.1f" % (anno_id,x,y))

        # Write out the ODD CSV file.
        ## The ODD CSV filename (and path).
        odd_csv_path = os.path.join(odd_path, "%s.csv" % (sub_id))
        #
        ## The CSV file string to write out.
        odd_csv_s = "annotation_id,x,y\n"
        #
        # Loop over the objects.
        for i, object_string in enumerate(object_list):
            odd_csv_s += object_string
            if i < len(object_list): odd_csv_s += "\n"
        #
        # Write out the CSV file.
        with open(odd_csv_path, "w") as nf:
            nf.write(odd_csv_s)

        lg.info(" * Subject '%s' found in '%s': % 6d annotations." % (sub_id, ann_csv_path, annotations.get_number_of_annotations()))

        print("* Converted '%s' -> '%s' (%d annotations)." % (ann_csv_path, odd_csv_path, annotations.get_number_of_annotations()))

    lg.info(" *")
    print("*")
