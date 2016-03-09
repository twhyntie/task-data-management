#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 MoEDAL and CERN@school - ANN -> NBL.

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
    print("* MoEDAL and CERN@school: ANN -> NBL *")
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

    ## The number of blobs data path.
    nbl_path = os.path.join(data_path, "NBL")
    if not os.path.isdir(nbl_path):
        os.mkdir(nbl_path)

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('./.', 'log_ann_to_nbl.log'), filemode='w', level=level)

    lg.info(" *")
    lg.info(" *====================================*")
    lg.info(" * MoEDAL and CERN@school: ANN -> NBL *")
    lg.info(" *====================================*")
    lg.info(" *")
    lg.info(" * Looking for annotations in             : '%s'" % (ann_path))
    lg.info(" * Writing number of blobs information in : '%s'" % (nbl_path))
    lg.info(" *")

    # Loop over the found annotations.
    for i, ann_csv_path in enumerate(sorted(glob.glob(os.path.join(ann_path, "*.csv")))):

        ## The subject ID.
        sub_id = os.path.basename(ann_csv_path)[:-4]

        ## The annotations found for the subject.
        annotations = ANN(ann_csv_path)

        ## A dictionary of the number of blobs identified in each annotation.
        #
        # { anno_id:number of blobs identified}
        num_blobs_dict = {}

        # Loop over the annotations found in the subject.
        for anno_id, anno in annotations.get_annotations().iteritems():

            # Get the number of blobs identified from the annotation.
            num_blobs = None

            ## The annotation data
            d = json.loads(anno)

            # Loop over the task answers for this annotation.
            for entry in d:

                if entry["task"] == "T2":

                    # Get the blob information from the annotation.
                    blob_answer = entry["value"]

                    if blob_answer == "No.":
                        num_blobs = 0

                elif entry["task"] == "T3":

                    # Get the blob information from the annotation.
                    blob_info = entry["value"]

                    # Add the number of blobs found in this annotation.
                    num_blobs = len(blob_info)

            num_blobs_dict[anno_id] = num_blobs

        # Write out the NBL CSV file.
        ## The NBL CSV filename (and path).
        nbl_csv_path = os.path.join(nbl_path, "%s.csv" % (sub_id))
        #
        ## The CSV file string to write out.
        nbl_csv_s = "annotation_id,n_blobs_identified\n"
        #
        # Loop over the blob counts.
        for i, anno_id in enumerate(sorted(num_blobs_dict)):
            nbl_csv_s += "%s,%d" % (anno_id, num_blobs_dict[anno_id])
            if i < len(num_blobs_dict): nbl_csv_s += "\n"
        #
        # Write out the CSV file.
        with open(nbl_csv_path, "w") as nf:
            nf.write(nbl_csv_s)

        lg.info(" * Subject '%s' found in '%s': % 6d annotations." % (sub_id, ann_csv_path, annotations.get_number_of_annotations()))

        print("* Converted '%s' -> '%s' (%d annotations)." % (ann_csv_path, nbl_csv_path, annotations.get_number_of_annotations()))

    lg.info(" *")
    print("*")
