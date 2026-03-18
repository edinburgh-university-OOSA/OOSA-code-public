

'''
Make geotiffs from an 
array of data, x and y
for a given resolution
'''

from pyproj import Proj, transform # package for reprojecting data
from osgeo import gdal             # pacage for handling geotiff data
from osgeo import osr              # pacage for handling projection information
import numpy as np



#####################################

def writeTiff(data,x,y,res,filename="lvis_image.tif",epsg=4326):
  '''
  Make a geotiff from an array of points
  '''

  # determine bounds
  minX=np.min(x)
  maxX=np.max(x)
  minY=np.min(y)
  maxY=np.max(y)

  # determine image size
  nX=int((maxX-minX)/res+1)
  nY=int((maxY-minY)/res+1)

  # pack in to array
  imageArr=np.full((nY,nX),-999.0)        # make an array of missing data flags

  # calculate the raster pixel index in x and y
  xInds=np.array(np.floor((x-np.min(x))/res),dtype=int)   # need to force to int type
  yInds=np.array(np.floor((np.max(y)-y)/res),dtype=int)
  # floor rounds down. y is from top to bottom

  # this is a simple pack which will assign a single footprint to each pixel
  imageArr[yInds,xInds]=data

  # set geolocation information (note geotiffs count down from top edge in Y)
  geotransform = (minX, res, 0, maxY, 0, -res)

  # load data in to geotiff object
  dst_ds = gdal.GetDriverByName('GTiff').Create(filename, nX, nY, 1, gdal.GDT_Float32)

  dst_ds.SetGeoTransform(geotransform)    # specify coords
  srs = osr.SpatialReference()            # establish encoding
  srs.ImportFromEPSG(epsg)                # WGS84 lat/long
  dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
  dst_ds.GetRasterBand(1).WriteArray(imageArr)  # write image to the raster
  dst_ds.GetRasterBand(1).SetNoDataValue(-999)  # set no data value
  dst_ds.FlushCache()                     # write to disk
  dst_ds = None

  print("Image written to",filename)
  return

