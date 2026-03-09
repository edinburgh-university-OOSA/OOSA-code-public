


'''
Make some data for
a pactical
'''

import numpy as np


#################################

def gauss(A,mu,sig,x):
  '''Return a Gaussian'''
  arg=((x-mu)**2)/(2*sig**2)
  y=A*np.exp(-1.0*arg)
  return(y)


#################################

def writeData(x,y,filename):
  '''Write data to a csv'''
  f=open(filename,'w')
  for i in range(0,len(x)):
    line=str(x[i])+","+str(y[i])+"\n"
    f.write(line)
  f.close()
  print("Data written to",filename)


#################################

if __name__=="__main__":
  '''main block'''

  # set the Gaussian parameters
  mus=[10,12,15,5,17]
  sigs=[2,0.5,1.2,1,0.3]
  As=[1,0.1,3,2.3,0.6]
  n=len(mus)

  # make the x array
  x=np.arange(-10,30,0.15)

  # make the Gaussians
  g=np.empty((n,x.shape[0]))
  for i in range(0,n):
    g[i]=gauss(As[i],mus[i],sigs[i],x)

  # add up Gaussians
  y=np.sum(g,axis=0)

  # save to a file
  writeData(x,y,'waveData.csv')

