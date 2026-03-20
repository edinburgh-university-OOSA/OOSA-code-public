

'''
A script to illustrate the
use of geopandas
Inspired by:  https://gist.github.com/nygeog/2731427a74ed66ca0e420eaa7bcd0d2b
'''

############################################

import argparse
import pandas as pd
import geopandas as gp
from shapely.geometry import Point


############################################

def readCommands():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("Handle a set of points in geopandas"))
  p.add_argument("--inEpsg", dest ="inEPSG", type=int, default=4326, help=("Input EPSG code"))
  p.add_argument("--outEpsg", dest ="outEPSG", type=int, default=27700, help=("Output EPSG code"))
  p.add_argument("--input", dest ="inName", type=str, default='../data/squirrel.csv', help=("Input filename"))
  p.add_argument("--output", dest ="outName", type=str, default='data.shp', help=("Output filename"))
  cmdargs = p.parse_args()
  return cmdargs


############################################

if __name__=="__main__":
  '''Main block'''

  # read the command line
  cmd=readCommands()
  inEPSG=cmd.inEPSG   # unpack to ease experimentation later
  outEPSG=cmd.outEPSG
  inName=cmd.inName
  outName=cmd.outName

  # read the file in to pandas dataframe
  df=pd.read_csv(inName)

  # sort by the time column
  sortedData=df.sort_values('time')

  # set up input and output projection as a dictionary
  s_crs={'init':'epsg:'+str(inEPSG)}
  t_crs={'init':'epsg:'+str(outEPSG)}

  # need to tell geopandas what the geometry of the data is
  geometry=[Point(xy) for xy in zip(df.lon,df.lat)]

  # put data in to geopandas dataframe
  geo_df=gp.GeoDataFrame(df,crs=s_crs,geometry=geometry)

  # check input projection
  print("Input projection is",geo_df.crs)

  # reproject
  reproj_df=geo_df.to_crs(t_crs)

  # write to a shapefile
  reproj_df.to_file(driver='ESRI Shapefile',filename=outName)
  print('Written to',outName,'in',t_crs)

  # NOTE: only the 'geometry' column has been reprojected, not the 'x' and 'y' arrays

