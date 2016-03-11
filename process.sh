#!/bin/bash
#
# The conversions.
python ann_to_nbl.py testdata/
python ann_to_nor.py testdata/
python ann_to_nir.py testdata/
python ann_to_nod.py testdata/
python ann_to_blb.py testdata/
python ann_to_ori.py testdata/
python ann_to_iri.py testdata/
python ann_to_odd.py testdata/
python ann_to_bkg.py testdata/
#
# Plotting.
python plot_nbl.py testdata/
python plot_nor.py testdata/
python plot_nir.py testdata/
python plot_nod.py testdata/
python plot_bkg.py testdata/
#
# Testing.
nose2
