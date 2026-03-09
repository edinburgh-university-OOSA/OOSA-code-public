
'''
Example of an array 
copying by pointer
'''


import numpy as np


if __name__=="__main__":
  '''The main block'''

  # make an array
  x=np.arange(0,10)

  # set a new array equal to the old
  y=x

  # this has copied the pointer reference, not the data
  print("\n\n## Pointer assignment ##\n")
  print("Original array before",x[2])
  # change a value in new array
  y[2]=103452
  # see what has changed
  print("New array after",y[2],"Original array after",x[2])
  print("The value has changed!")

  # to copy the data to a new pointer
  y=np.copy(x)

  # this has copied the data to a new memory space
  print("\n\n## np.copy() ##\n")
  print("Original array before",x[3])
  # change a value in new array
  y[3]=103452
  # see what has changed
  print("New array after",y[3],"Original array after",x[3])
  print("The value has not changed!")



  # this has implciations for passing to a function
  print("\n\n## function() passing ##\n")

  def someFunc(x,y):
    '''A function which takes a number and an array'''
    x=4
    y[0]=4

  x=3                # an integer
  y=np.arange(0,10)  # an array

  # pass data to the function
  someFunc(x,y)

  # see what has changed
  print("X is now",x,"y[0] is now",y[0])
  print("The number did not change, the array did")
  print("A number is copied when passed to a function. An array passes a pointer to RAM space")

  print("\n\n")

