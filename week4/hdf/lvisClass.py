
'''
A class to hold LVIS data
with methods to read
'''

###################################
import numpy as np
import h5py


###################################

class lvisData(object):
  '''
  LVIS data handler
  '''

  def __init__(self,filename,setElev=False,minX=-100000000,maxX=100000000,minY=-1000000000,maxY=100000000,onlyBounds=False):
    '''
    Class initialiser. Calls a function
    to read LVIS data within bounds
    minX,minY and maxX,maxY
    setElev=1 converts LVIS's stop and start
    elevations to arrays of elevation.
    onlyBounds sets "bounds" to the corner of the area of interest
    '''
    # call the file reader and load in to the self
    self.readLVIS(filename,minX,minY,maxX,maxY,onlyBounds)
    if(setElev):     # to save time, only read elev if wanted
      self.setElevations()


  ###########################################

  def readLVIS(self,filename,minX,minY,maxX,maxY,onlyBounds):
    '''
    Read LVIS data from file
    '''
    # open file for reading
    f=h5py.File(filename,'r')
    # determine how many bins
    self.nBins=f['RXWAVE'].shape[1]
    # read coordinates for subsetting
    lon0=np.array(f['LON0'])       # longitude of waveform top
    lat0=np.array(f['LAT0'])       # lattitude of waveform top
    lonN=np.array(f['LON'+str(self.nBins-1)]) # longitude of waveform bottom
    latN=np.array(f['LAT'+str(self.nBins-1)]) # lattitude of waveform bottom
    # find a single coordinate per footprint
    tempLon=(lon0+lonN)/2.0
    tempLat=(lat0+latN)/2.0

    # write out bounds and leave if needed
    if(onlyBounds):
      self.lon=tempLon
      self.lat=tempLat
      self.bounds=self.dumpBounds()
      return

    # dertermine which are in region of interest
    useInd=np.where((tempLon>=minX)&(tempLon<maxX)&(tempLat>=minY)&(tempLat<maxY))
    if(len(useInd)>0):
      useInd=useInd[0]

    if(len(useInd)==0):
      print("No data contained in that region")
      self.nWaves=0
      return

    # save the subset of all data
    self.nWaves=len(useInd)
    self.lon=tempLon[useInd]
    self.lat=tempLat[useInd]

    # load sliced arrays, to save RAM
    self.lfid=np.array(f['LFID'][useInd])          # LVIS flight ID number
    self.lShot=np.array(f['SHOTNUMBER'][useInd])   # the LVIS shot number, a label
    self.waves=np.array(f['RXWAVE'][useInd])       # the recieved waveforms. The data
    self.nBins=self.waves.shape[1]
    # these variables will be converted to easier variables
    self.lZN=np.array(f['Z'+str(self.nBins-1)][useInd])       # The elevation of the waveform bottom
    self.lZ0=np.array(f['Z0'][useInd])          # The elevation of the waveform top
    # close file
    f.close()
    # return to initialiser
    return


  ###########################################

  def setElevations(self):
    '''
    Decodes LVIS's RAM efficient elevation
    format and produces an array of
    elevations per waveform bin
    '''
    self.z=np.empty((self.nWaves,self.nBins))
    for i in range(0,self.nWaves):    # loop over waves
      self.z[i]=np.linspace(self.lZ0[i],self.lZN[i],self.nBins)   # returns an array of floats


  ###########################################

  def getOneWave(self,ind):
    '''
    Return a single waveform
    '''
    return(self.z[ind],self.waves[ind])


  ###########################################

  def dumpCoords(self):
     '''
     Dump coordinates
     '''
     return(self.lon,self.lat)

  ###########################################

  def dumpBounds(self):
     '''
     Dump bounds
     '''
     return[np.min(self.lon),np.min(self.lat),np.max(self.lon),np.max(self.lat)]  # this returns a list
                                                                                  # rather than a tuple ()

###########################################

