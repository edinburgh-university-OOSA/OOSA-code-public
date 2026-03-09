
'''
A class to build on 
and produce a binary
search algorithm
'''

import numpy as np
from sys import exit
import matplotlib.pyplot as plt


#####################################

class dataSorter(object):
  '''A class to hold data and provide examples of search algorithms'''

  def __init__(self,numb=100):
    '''Class initialiser'''
    self.numb=numb
    self.arr=np.random.random((numb))

  def sortArray(self):
    '''Sort an array of data'''
    self.sorted=np.sort(self.arr)
    return

  def plotSorted(self,filename='plt.png'):
    '''Plot the sorted array. It has a default name'''
    plt.plot(self.sorted)
    plt.savefig(filename)
    plt.xlabel('Array position')
    plt.ylabel('Array value')
    plt.cla()
    print("Graph drawn to",filename)
    return


#####################################

if __name__ == "__main__":
  '''Main block'''

  data=dataSorter(numb=100) # initialise class
  data.sortArray()          # sort random numbers
  data.plotSorted(filename='thisPlot.png')  # plot data

