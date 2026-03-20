# Public code for the OOSA course.

This is the repository for the University of Edinburgh's [OOSA](https://www.drps.ed.ac.uk/25-26/dpt/cxpgge11106.htm) course. There is a separate directory for each week's work. As we progress, suggested answers will be uploaded.


## Foundations

The **foundations** folder contains some warm up exercises to transition on to the course. There are two folders within:

* basic\_features
* iterating

The basic\_features folder contains a set of scripts introducing the basic Python features (data types, loops, plotting etc.). Other than **06_objects.py**, which will be covered in week 2, these should already be familar to you and are included here for revision.

The **iterating** directory contains some exercises to practice using loops and work up to moving around a raster dataset.


## Week 1

Week 1 covers:

***Aspects***
* Github version control and code repository
* Computer basics 
* Revision of loops and file I/O

***Algorithm***
* Introduction to algorithm design: Finding minima and sorting


### fileIO

Contains two scripts to demonstrate reading from a text file and writing to a text file. The ***data*** folder contains the data for the file reading example.


### data

Contains a text file with some sample data to practice reading with the fileIO code.


### sort

Contains an example solution for a simple sort algorithm. Note that there are multiple sort solutions, such as bubble sort, and then many more complex and efficient algorithms.



## Week 2

Week 2 covers

***Aspects***
* Using the command line to make programmable programs
* Objects and classes

***Algorithm***
* Binary search: Loop and recursion


### main

Contains an example of the main block in order to ease importing code in to other programs



### command\_line

Contains two example python files, which can be used to alter the behaviour of a program at run time. This allows you to create a single python program and then reuse it with different input files, options etc.

    commandExample.py: Minimum workable example of a command line
    commandLineIllus.py: Illustrates the common command

The options for commandLineIllus.py are:

    -h, --help            show this help message and exit
    --input INNAME        Input filename Default=test.txt
    --lat LAT             Latitude in degrees Default = 5
    --max_vcf MAXVCF      Maximum VCF value to use Default = 100
    --useSnow             Use snow switch Default = False
    -p [POW_BEAM_LIST ...], --power_beams [POW_BEAM_LIST ...] Track numbers of power beams Default = 5 and 6



### objects

Includes a script with a simple example of an object; a grouping of data and functions.


### data

Contains some text data files for use in this week's exercises.



### docu\_strings

Contains a piece of code demonstrating the suggested use of document string comments.


### binary\_search

Contains code to teach about increasing efficiency via the example of a binary search.

    searchObject.py:            begins an object for sorting data
    searchObject_withplot.py:   the above with an plotting function added
    binarySearches.py:          contains suggested answers for binary search by loop and recursion
    finishedQuartiles.py:       week 2 algorithm solution. uses the above to find quartiles in a sorted dataset


The scripts below create the test data.

    makeData.py:                makes data for testing algorithms
    randomWages.py:             generates random wage data for testing algorithms


## Week 3

Week 3 covers

***Aspects*** 
* Geospatial packages: pyproj and gdal
* A note on function input/output
* Function fitting
* A mention of pandas

***Algorithm***
* Douglas-Peucker line generalization


### docu\_strings

Contains examples of document strings.


### reproject

Shows an example of using the gdal package to reproject raster or vector data.


### function\_fit

Shows an example of fitting a function to data.


### pointer\_reference

Demonstrates the difference between variables that point to an array and copying a whole array.


### pandas

Shows an example of reading data into a pandas object.


### line\_distance

A function to find the orthogonal distance between a line and a point, to be used in the Douglas-Peucker line generalization algorithm.

### dp-line-general
    
Contains an example solution for the Douglas-Peucker line generalisation.



## Week 4

Week 4 covers

***Aspects***
* Geospatial data formats; HDF5


### hdf

This folder contains some starter code to handle HDF5 formatted data from the LVIS lidar.

    lvisClass.py -   The base class to read LVIS data into RAM
    lvisExample.py - An example of using lvisClass.py
    processLVIS.py - Inherits from lvisClass.py and adds methods to extract ground elevation
    lvisCompleteExample.py - example solutions for the week 4 tasks

Takes the following input parameters

    --input INNAME     LVIS input filename
    --outRoot OUTROOT  Output filename root to use with graphs and DEMs produced.


### geotiff

This contains a script with a function to take an array of vector data (x,y,z) and produces a raster of the z values at a given resolution:

    tiffExample.py


## Week 5

Week 5 covers
    
***Aspects***
* More geospatial packages: Geopandas
* RAM management
* A brief introduction to machine learning

***Algorithm***
* Machine learning; getting data into the machine


### geopandas
    
This folder contains an example of using geopandas to read a csv file containing geographic data, sorting and reprojecting it. Note that it makes use of the **shapely** package to define the geometry type within the geopandas array. Here **Point** is used as this is vector data. This stacking of packages can be difficult to follow, but the answers can be found on the documentation and stackoverflow. The latter is sometimes more helpful for specific tasks, as the official documentation shows all possible uses.
    
   week5/geopandas/geopandasExample.py
    
This script has the following command line options:

    --inEpsg INEPSG    Input EPSG code
    --outEpsg OUTEPSG  Output EPSG code
    --input INNAME     Input filename
    --output OUTNAME   Output filename


### RAM management

To illstrate RAM management, a stack of rasters will be processed. You can use the *readTiff.py* script from week 4 as starter code. This uses GDAL to read in a raster file, has a space to perform some data manipulation, and writes out the result.



### Function fitting

This section gives examples for linear and polynomial fitting, to illustrate the components that go into machine learning. The code includes

    linearFit.py           # linear fitting example
    linearFit_answer.py    # linear fitting wth task answers
    polyFit.py             # polynomial fitting example
    polyFit_answer.py      # polynomial fitting with task answers
    aic_answer.py          # polynomial fitting with AIC task answers


### Machine learning

A simple example is available in

    week5/random_forest/randomForest_example.py

It has the following options:

    --input NAMEN         Input data table
    --trainFrac TRAINFRAC Fraction of data to use for training
    --nTrees N_ESTIMATORS Number of trees
    --max_depth MAX_DEPTH Maximum branch depth


A more complex example is available that brings together all parts of the course. Note that this is not working as yet due to a bug in the data reading. This code is taken from Euan Mitchell's [dissertation repository](https://github.com/euanmitchell/dissertation)

    week5/random_forest/randomForestLaSelva.py





# Dependencies

The code in these repositories make use of the following packages and is all in python3:

    numpy
    matplotlib.pylot
    h5py
    pyproj
    gdal
    rasterio
    argparse
    sklearn


# Author

steven.hancock@ed.ac.uk

