
'''
Examples of binary search
by loop and by recursion
'''


#############################################

def binarySearch(x,v):
  '''Binary search for v in x by looping'''

  # set first break point and ends
  start=0              # the start index
  end=len(x)           # the end index
  midP=(start+end)//2  # the mid point

  # a flag to let us know if the exact number has been found
  foundExact=False

  # loop over
  while((end-start)>1):
    if(x[midP]<v):   # answer is to the right
      start=midP
      midP=(start+end)//2
    elif(x[midP]>v):   # answer is to the left
      end=midP
      midP=(start+end)//2 
    elif(x[midP]==v):  # found answer, unlikely
      foundExact=True  # have found exact answer
      break

  # if we have not found the exact answer, find the closest element
  if(foundExact==False):
    sep=np.abs(x[start:end]-v)  # use a slice to find the absolute distance
    midP=sep.argmin()+start     # set mid point as element with smallest distance

  return(x[midP],midP)


#############################################

def binaryRecurse(x,v,start,end):
  '''Binary search for v in x by recursion'''

  # set first break point and ends
  ind=(start+end)//2 # middle point index
  thisVal=x[ind]

  # Once we have two elements left, both have been checked and neither is exact
  if((end-start)<=1):
    # we can find the closest of the two to our value
    sep=np.abs(x[start:end]-v)  # use a slice to find the absolute distance
    ind=sep.argmin()+start      # set mid point as element with smallest distance
    thisVal=x[ind]
    return(thisVal,ind)

  if(thisVal<v):   # to the right
    thisVal,ind=binaryRecurse(x,v,ind,end)
  elif(thisVal>v):   # answer is to the left
    thisVal,ind=binaryRecurse(x,v,start,ind)
  elif(thisVal==v):  # found answer, unlikely
    return(thisVal,ind)

  return(thisVal,ind)


###################################

if __name__=="__main__":
  '''Main block'''
  import numpy as np

  # generate an array
  jimlad=np.random.random((1000))

  # sort the array
  jimlad=np.sort(jimlad)

  # recursion
  thisVal,ind=binaryRecurse(jimlad,0.3,0,jimlad.shape[0])
  print("Recursion",thisVal,ind)

  # loop
  thisVal,ind=binarySearch(jimlad,0.3)
  print("While loop",thisVal,ind)

