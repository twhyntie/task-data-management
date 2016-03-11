#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 MoEDAL and CERN@school - ANN -> NOD.

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
    print("* MoEDAL and CERN@school: ANN -> NOD *")
    print("*====================================*")
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

    ## The annotations path.
    ann_path = os.path.join(data_path, "ANN")
    if not os.path.isdir(ann_path):
        raise IOError("* ERROR: '%s' does not exist - no annotation data!" % (ann_path))

    ## The number of oddities data path.
    nod_path = os.path.join(data_path, "NOD")
    if not os.path.isdir(nod_path):
        os.mkdir(nod_path)

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('./.', 'log_ann_to_nod.log'), filemode='w', level=level)

    lg.info(" *")
    lg.info(" *====================================*")
    lg.info(" * MoEDAL and CERN@school: ANN -> NOD *")
    lg.info(" *====================================*")
    lg.info(" *")
    lg.info(" * Looking for annotations in                : '%s'" % (ann_path))
    lg.info(" * Writing number of oddities information in : '%s'" % (nod_path))
    lg.info(" *")

    # Loop over the found annotations.
    for i, ann_csv_path in enumerate(sorted(glob.glob(os.path.join(ann_path, "*.csv")))):

        ## The subject ID.
        sub_id = os.path.basename(ann_csv_path)[:-4]

        ## The annotations found for the subject.
        annotations = ANN(ann_csv_path)

        ## A dictionary of the number of oddities identified in each annotation.
        #
        # { anno_id:number of oddities identified}
        num_oddities_dict = {}

        # Loop over the annotations found in the subject.
        for anno_id, anno in annotations.get_annotations().iteritems():

            # Get the number of outer rings identified from the annotation.
            num_oddities = None

            ## The annotation data
            d = json.loads(anno)

            # Loop over the task answers for this annotation.
            for entry in d:

                if entry["task"] == "T6":

                    # Get the oddity information from the annotation.
                    oddity_answer = entry["value"]

                    if oddity_answer == "No.":
                        num_oddities = 0

                elif entry["task"] == "T7":

                    # Get the oddity information from the annotation.
                    oddity_info = entry["value"]

                    # Add the number of oddities found in this annotation.
                    num_oddities = len(oddity_info)

            num_oddities_dict[anno_id] = num_oddities

        # Write out the NOD CSV file.
        ## The NOD CSV filename (and path).
        nod_csv_path = os.path.join(nod_path, "%s.csv" % (sub_id))
        #
        ## The CSV file string to write out.
        nod_csv_s = "annotation_id,n_oddities_identified\n"
        #
        # Loop over the outer ring counts.
        for i, anno_id in enumerate(sorted(num_oddities_dict)):
            nod_csv_s += "%s,%d" % (anno_id, num_oddities_dict[anno_id])
            if i < len(num_oddities_dict): nod_csv_s += "\n"
        #
        # Write out the CSV file.
        with open(nod_csv_path, "w") as nf:
            nf.write(nod_csv_s)

        lg.info(" * Subject '%s' found in '%s': % 6d annotations." % (sub_id, ann_csv_path, annotations.get_number_of_annotations()))

        print("* Converted '%s' -> '%s' (%d annotations)." % (ann_csv_path, nod_csv_path, annotations.get_number_of_annotations()))

    lg.info(" *")
    print("*")
