

'''
Week 3 quartile task
'''

import argparse
import numpy as np
from sys import exit
from binarySearches import *
from searchObject import dataSorter


##########################################################

class newSorter(dataSorter):
  '''
  Class to hold and manipulate data
  '''

  def __init__(self,filename):
    '''Initialise by reading data from a file'''
    self.wage,self.age=np.loadtxt(filename,delimiter=',',usecols=(0,1),unpack=True,dtype=float,comments="#")
    self.doneSort=False   # a flag to say if we have sorted yet or not
    self.arr=self.wage   # here we are interested in the wage array


  def findQuartile(self,thisW):
    '''Find a quartile of percentage q'''

    # if not already sorted, then sort
    if(self.doneSort==False):
      self.sortArray()

    # binary search
    w,thisQ=binarySearch(self.sortArr,thisW)  # loop

    # return the quantile
    return((thisQ/self.sortArr.shape[0])*100)



##########################################################

def readCommands():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("Reads in some data and finds quartiles"))
  p.add_argument("--wage", dest ="wage", type=float, default=27000, help=("Wage to determine the quantile of. Default is 27,000"))
  p.add_argument("--input", dest ="inName", type=str, default="../data/wages.csv", help=("Input file to read data rom. Default is ../data/wages.csv"))
  cmdargs = p.parse_args()
  return cmdargs


##########################################################

if __name__=="__main__":
  '''The main block'''

  # read the command line
  com=readCommands()

  # read data in to object
  filename=com.inName
  dataObj=newSorter(filename)

  # print to show it is working
  print("Data read from",filename)
  print("Mean wage is",np.mean(dataObj.wage))

  # sort it
  dataObj.sortArray()

  # find quartiles
  qList=[25,50,75]
  for q in qList:
    thisW=dataObj.sortArr[int((q/100)*dataObj.sortArr.shape[0])]
    print(q,"quartile is %.0f"%(thisW))  # note the use of %.0f to give decimal places

  # now find what quartile a particular wage occurs in
  thisQ=dataObj.findQuartile(com.wage)
  print("%.0f is in the %.1f quartile"%(com.wage,thisQ))  # again note %.1f to control decimal places

