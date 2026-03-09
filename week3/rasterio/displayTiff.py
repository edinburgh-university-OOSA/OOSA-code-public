
'''
Example of opening and 
displaying a raster with
rasterio
'''

# This example was inspired by:
# https://rasterio.readthedocs.io/en/latest/quickstart.html

# import packages needed
import rasterio
import matplotlib.pyplot as plt


#################################

if __name__ == "__main__":
  '''Main block'''

  # set a file
  filename='/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12/T30VVH_A020126_20210112T113447_B08.jp2'

  # open it as a rasterio object
  dataset=rasterio.open(filename)

  # print out some properties of it
  print("The image is",dataset.width,"by",dataset.height,"pixels")
  print("The projection is",dataset.crs)

  # read the raster data into RAM
  bandLayer=dataset.read(1)

  # print to the screen
  plt.imshow(bandLayer)
  plt.show()

