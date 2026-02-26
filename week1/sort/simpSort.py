

'''
Simple sorting function
This is simple sort
Other sorting algortithms
are available.
'''

import numpy as np
from datetime import datetime



###############################################

def findMin(arr):
  '''A minimum funding function'''
  minN=10000  # a big number
  minInd=0
  for i in range(0,arr.shape[0]):
    if(arr[i]<minN):
      minN=arr[i]
      minInd=i
  return(minN,minInd)


###########################################

if __name__ == '__main__':

  # Make array of data
  arr=np.random.random((100))

  # make space for sorted array
  sortArr=np.empty(arr.shape)

  # copy array so we can modify without overwriting
  copArr=np.copy(arr)

  # sort the array
  for i in range(0,copArr.shape[0]):
    minN,minInd=findMin(copArr)
    sortArr[i]=minN
    copArr[minInd]=1000000


  # write to a file
  filename="x.txt"
  f=open(filename,"w")
  for i in sortArr:
    line=str(i)+"\n"
    f.write(line)

  f.close()
  print("Written to",filename)

