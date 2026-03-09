

#################################
"""
A simple example of 
reprojecting data
with pyproj
"""
#################################


# import necessary functions
import numpy as np
from pyproj import Transformer
import argparse


#################################

def readCommands():
  '''
  Get commandline arguments
  '''
  p = argparse.ArgumentParser(description=("Example of reprojecting data with pyproj."), formatter_class=argparse.RawTextHelpFormatter)
  p.add_argument("--numb", dest ="numb", type=int, default=5, help=("Number of coordinates to make\nDefault = 5"))
  p.add_argument("--outEPSG", dest ="outEPSG", type=int, default=27700, help=("EPSG of input data\nDefault = 27700"))
  cmdargs = p.parse_args()
  return cmdargs


#################################

def makeUpCoords(numb):
  """Make an array of random coordimates"""
  # bounds of UK in EPSG:4326
  minLat=49.96
  maxLat=60.84
  minLon=-7.5
  maxLon=1.78
  # generate array of random numbers
  lon=np.random.rand(numb)*(maxLon-minLon)+minLon
  lat=np.random.rand(numb)*(maxLat-minLat)+minLat
  return(lon,lat)


#################################

def reprojectData(lon,lat,outEPSG):
  # set projections

  # define projections
  reproject = Transformer.from_crs(4326,outEPSG,always_xy=True)

  # reproject data
  x,y=reproject.transform(lon,lat)

  return(x,y)


#################################

def dumpResults(x,y,lon,lat):
  """Dump results to the screen"""
  for i in range(0,len(x)):
    print(x[i],y[i],"lonlat",lon[i],lat[i])
  return


#################################
# main

if __name__ == '__main__':
  cmdArgs=readCommands()
  # make an array of coords in UK
  lon,lat=makeUpCoords(cmdArgs.numb)
  # reproject the data
  x,y=reprojectData(lon,lat,cmdArgs.outEPSG)
  # dump results to screen
  dumpResults(x,y,lon,lat)

