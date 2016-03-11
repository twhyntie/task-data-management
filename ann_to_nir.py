#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 MoEDAL and CERN@school - ANN -> NIR.

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
    print("* MoEDAL and CERN@school: ANN -> NIR *")
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

    ## The number of inner rings data path.
    nir_path = os.path.join(data_path, "NIR")
    if not os.path.isdir(nir_path):
        os.mkdir(nir_path)

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join('./.', 'log_ann_to_nir.log'), filemode='w', level=level)

    lg.info(" *")
    lg.info(" *====================================*")
    lg.info(" * MoEDAL and CERN@school: ANN -> NIR *")
    lg.info(" *====================================*")
    lg.info(" *")
    lg.info(" * Looking for annotations in                   : '%s'" % (ann_path))
    lg.info(" * Writing number of inner rings information in : '%s'" % (nir_path))
    lg.info(" *")

    # Loop over the found annotations.
    for i, ann_csv_path in enumerate(sorted(glob.glob(os.path.join(ann_path, "*.csv")))):

        ## The subject ID.
        sub_id = os.path.basename(ann_csv_path)[:-4]

        ## The annotations found for the subject.
        annotations = ANN(ann_csv_path)

        ## A dictionary of the number of inner rings identified in each annotation.
        #
        # { anno_id:number of inner rings identified}
        num_inner_rings_dict = {}

        # Loop over the annotations found in the subject.
        for anno_id, anno in annotations.get_annotations().iteritems():

            # Get the number of inner rings identified from the annotation.
            num_inner_rings = None

            ## The annotation data
            d = json.loads(anno)

            # Loop over the task answers for this annotation.
            for entry in d:

                if entry["task"] == "T4":

                    # Get the ring information from the annotation.
                    ring_answer = entry["value"]

                    if ring_answer == "No.":
                        num_inner_rings = 0

                elif entry["task"] == "T1":

                    # Get the inner ring information from the annotation.
                    inner_ring_info = entry["value"]

                    # Add the number of inner rings found in this annotation.
                    num_inner_rings = len(inner_ring_info)

            num_inner_rings_dict[anno_id] = num_inner_rings

        # Write out the NIR CSV file.
        ## The NIR CSV filename (and path).
        nir_csv_path = os.path.join(nir_path, "%s.csv" % (sub_id))
        #
        ## The CSV file string to write out.
        nir_csv_s = "annotation_id,n_inner_rings_identified\n"
        #
        # Loop over the inner ring counts.
        for i, anno_id in enumerate(sorted(num_inner_rings_dict)):
            nir_csv_s += "%s,%d" % (anno_id, num_inner_rings_dict[anno_id])
            if i < len(num_inner_rings_dict): nir_csv_s += "\n"
        #
        # Write out the CSV file.
        with open(nir_csv_path, "w") as nf:
            nf.write(nir_csv_s)

        lg.info(" * Subject '%s' found in '%s': % 6d annotations." % (sub_id, ann_csv_path, annotations.get_number_of_annotations()))

        print("* Converted '%s' -> '%s' (%d annotations)." % (ann_csv_path, nir_csv_path, annotations.get_number_of_annotations()))

    lg.info(" *")
    print("*")
