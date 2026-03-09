

'''
Generates random wages
and adds to a file
'''

import numpy as np
from scipy.stats import skewnorm


numb=1000
minW=987
meanW=29000
maxW=110000

m=(maxW-minW)/55
c=-1*18*m

# generate wages
w=np.random.normal(loc=meanW,scale=(maxW-meanW)/5.0,size=(numb))

# generate ages
a=(w-c)/m

# add some noise
a=a+np.random.normal(loc=0.0,scale=10.0,size=(numb))

# which are realistic
useInd=np.where((a>13)&(w>10))[0]


# write to a file
filename='wages.csv'
f=open(filename,'w')

for i in useInd:
  line=str(w[i])+","+str(a[i])+"\n"
  f.write(line)

f.close()
print("Written to",filename)

