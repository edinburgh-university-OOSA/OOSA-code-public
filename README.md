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




# Dependencies

The code in these repositories make use of the following packages and is all in python3:

    numpy
    matplotlib.pylot
    h5py
    pyproj
    gdal
    rasterio


# Author

steven.hancock@ed.ac.uk

