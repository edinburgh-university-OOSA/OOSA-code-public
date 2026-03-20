

'''
Finds a line of best fit
to scatter data
'''


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress   # import only the one function for speed


##################################

class dataFit(object):
  '''
  Class to hold our
  data and methods
  '''

  def __init__(self,filename):
    '''Read data from file and store'''
    self.wage,self.age=np.loadtxt(filename,delimiter=',',usecols=(0,1),unpack=True,dtype=float,comments="#")


  def fitLine(self):
    '''Fit a straight line through data and determine statistics'''
    # straight line coefficients. See scipy.stats.linregress() documentation
    result=linregress(self.age,y=self.wage)
    self.m=result[0]   # gradient
    self.c=result[1]   # intercept
    self.R=result[2]   # R^2
    # other metrics are available
    print("R-squared is",self.R)


  def plotLine(self,outName):
    '''Plot our line of best fit'''

    # add a method to plot the line of best fit
    # note that you will need to make the line in variables

    return


##################################

if __name__=="__main__":
  '''The main block'''

  # read data in to object
  filename="../data/wages.csv"
  dataObj=dataFit(filename)

  # fit line
  dataObj.fitLine()

  # plot it
  outName="linePlot.png"
  dataObj.plotLine(outName)

