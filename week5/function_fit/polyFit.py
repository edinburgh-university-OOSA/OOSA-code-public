

'''
Finds a polynomial line of 
best fit to scatter data
'''


import argparse
import numpy as np
import matplotlib.pyplot as plt


##################################

def readCommands():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("Handle a set of points in geopandas"))
  p.add_argument("--order", dest ="order", type=int, default='1', help=("Order of polynomial to fit"))
  p.add_argument("--input", dest ="filename", type=str, default="../data/polyData.txt", help=("Input filename"))
  cmdargs = p.parse_args()
  return cmdargs


##################################

class dataFit(object):
  '''
  Class to hold our
  data and methods
  '''

  def __init__(self,filename):
    '''Read data from file and store'''
    self.x,self.y=np.loadtxt(filename,usecols=(0,1),unpack=True,dtype=float,comments="#")


  ####################################

  def fitPoly(self,order):
    '''Fit a polynomial line through data and determine statistics with a given order'''

    # fit a polynomial line and save the parameters
    self.p=np.polyfit(self.x,self.y,order)

    return

  ####################################

  def plotLine(self,outName):
    '''Plot our line of best fit'''

    # make the line
    minX=np.min(self.x)
    maxX=np.max(self.x)
    x=np.linspace(minX,maxX,num=200)

    # producy a polynomial using the polyval function
    y=np.polyval(self.p, x)

    # plot the two
    plt.plot(self.x,self.y,'.')
    plt.plot(x,y)
    plt.xlabel('Y value (units)')
    plt.ylabel('X value (units)')
    plt.savefig(outName) # write the graph to a file
    plt.close()           # close the file
    plt.clf()             # clear everything so we can start a new plot
    print("Graph drawn to",outName)


##################################

if __name__=="__main__":
  '''The main block'''

  # read the command line
  cmd=readCommands()

  # read data in to object
  dataObj=dataFit(cmd.filename)

  # fit line
  dataObj.fitPoly(cmd.order)

  # determine the accuract of the fit

  # plot it
  outName="linePlot.png"
  dataObj.plotLine(outName)

