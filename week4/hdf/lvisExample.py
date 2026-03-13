
'''
An example of how to use the 
LVIS python scripts
'''

# import the HDF5 data handler class

from lvisClass import lvisData



##########################################

class plotLVIS(lvisData):
  '''A class, ineriting from lvisData
     and add a plotting method'''

  def reprojectLVIS(self,outEPSG):
    '''A method to reproject the geolocation data'''
    # method incomplete


  def plotWaves(self):
    '''A method to plot all waveforms'''
    # this needs completing



##########################################


if __name__=="__main__":
  '''Main block'''

  filename='/geos/netdata/oosa/week4/lvis_antarctica/ILVIS1B_AQ2015_1014_R1605_070717.h5'

  # create instance of class with "onlyBounds" flag
  b=plotLVIS(filename,onlyBounds=True)

  # to make a MWE,
  # from the total file bounds
  # choose a spatial subset
  x0=b.bounds[0]
  y0=b.bounds[1]
  x1=(b.bounds[2]-b.bounds[0])/20+b.bounds[0]
  y1=(b.bounds[3]-b.bounds[1])/20+b.bounds[1]


  # read in all data within our spatial subset
  lvis=plotLVIS(filename,minX=x0,minY=y0,maxX=x1,maxY=y1)

  # set elevation
  lvis.setElevations()


  # reproject the data

  # plot up some waveforms using your new method

