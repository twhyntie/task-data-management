#The MoEDAL TASL Raw Scan Images: Metadata Schema
Yhis document describes the metadata schema for
the MoEDAL TASL Raw Scan Images.

##Overview
This data format describes the raw scan images of the Nuclear Track Detector (NTD) sheets provided by TASL.

##The records
Each record represented by this metadata schema represents an image file provided by TASL. Each image is a montage of all accepted 'tracks' (pits) and their position coordinates from a particular scan after TASL's discrimination filters have been applied. 

##The elements
* [ID](#id) (`id`)
* [Batch ID](#batch_id) (`batch_id`)
* [Experiment](#experiment) (`experiment`)
* [Owner](#owner) (`owner`)
* [Filename](#filename) (`filename`)
* [File format](#file_format) (`file_format`)
* [Data format](#data_format) (`data_format`)
* [Image width](#image_width) (`image_width`)
* [Image height](#image_height) (`image_height`)
* [File size](#file_size) (`file_size`)
* [Number of individual scan rows](#n_scan_rows) (`n_scan_rows`)
* [Number of individual scan columns](#n_scan_columns) (`n_scan_columns`)
* [Number of individual scan images](#n_scans) (`n_scans`)
* [Scan magnification](#magnification) (`magnification`)

The element details are provided in the subsections below.

###<a name='id'>ID</a>
The record ID.
* _Field name_: `id`
* _Format_: a string
* _Required?_ Yes.

###<a name='batch_id'>Batch ID</a>
The ID of the batch to which the scan belongs.
* _Field name_: `batch_id`
* _Format_: a string
* _Required?_ Yes.

###<a name='experiment'>Experiment</a>
The experiment to which the data belongs.
* _Field name_: `experiment`
* _Format_: a string
* _Required?_ Yes.

###<a name='owner'>Owner</a>
The owner of the data.
* _Field name_: `owner`
* _Format_: a string
* _Required?_ Yes.

###<a name='filename'>Filename</a>
The filename of the file represented by the record.
* _Field name_: `filename`
* _Format_: a posix compliant filename (string)
* _Required?_ Yes.

###<a name='file_format'>File format</a>
The file format of the image.
* _Field name_: `file_format`
* _Format_: a string
* _Required?_ Yes.

###<a name='data_format'>Data format</a>
The data format code (with respect to the data management plan).
* _Field name_: `data_format`
* _Format_: a three-letter string
* _Required?_ Yes.

###<a name='image_width'>Image width</a>
The width of the image in pixels.
* _Field name_: `image_width`
* _Units_: pixels
* _Format_: an integer
* _Required?_ Yes.

###<a name='image_height'>Image height</a>
The height of the image in pixels.
* _Field name_: `image_height`
* _Units_: pixels
* _Format_: an integer
* _Required?_ Yes.

###<a name='file_size'>File size</a>
The size of the file represented by the record in bytes.
* _Field name_: `file_size`
* _Units_: bytes
* _Format_: an integer
* _Required?_ Yes.

###<a name='n_scan_rows'>Number of individual scan rows</a>
The TASL scan images contain multiple pit candidate images
arranged in a table. This element records the number of rows
in the file.
* _Field name_: `n_scan_rows`
* _Format_: an integer
* _Required?_ Yes.

###<a name='n_scan_columns'>Number of individual scan columns</a>
The TASL scan images contain multiple pit candidate images
arranged in a table. This element records the number of rows
in the file.
* _Field name_: `n_scan_columns`
* _Format_: an integer
* _Required?_ Yes.

###<a name='n_scans'>Number of individual scan images</a>
The TASL scan images contain multiple pit candidate images
arranged in a table. This element records the number of scans
in the file. Note that this will not necessarily be the
rows multiplied by the columns as not every space in the
table is full.
* _Field name_: `n_scans`
* _Format_: an integer
* _Required?_ Yes.

###<a name='magnification'>Scan magnification</a>
The magnification at which the scan was taken.
* _Field name_: `magnification`
* _Format_: a floating point number
* _Required?_ Yes.

