
################################
# Illustration of a main block #
################################

# modules needed
import numpy as np


################################
# define a function, a simple mean here

def getMean(x):
  mean=np.mean(x)
  return(mean)


################################
# the main block

if __name__ == '__main__':
  # create some data
  data=np.random.rand(100)
  # call our function
  meanX=getMean(data)
  print("Mean is",meanX)


# the end
################################

