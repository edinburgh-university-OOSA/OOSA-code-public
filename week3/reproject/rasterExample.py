
'''
Example of reprojecting 
a raster
'''

from osgeo.gdal import Warp


#########################

if __name__=="__main__":
  '''Main'''
  # set input/output (could be done on command line)
  inName='/geos/netdata/oosa/week3/raster/discRefl.LT.refl.tif'
  outName='warped.tif'
  # EPSG to project oo
  outEPSG='4326'
  # reproject to new file (could output to an object instead)
  Warp(outName,inName,dstSRS='EPSG:'+outEPSG)
  # many more options available
  # https://gdal.org/python/osgeo.gdal-module.html#Warp

