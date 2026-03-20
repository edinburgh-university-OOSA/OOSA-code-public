
'''
An example of Random Forest
'''

import argparse
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


#################################################

def readCommands():
    '''
    Read the arguments passed from the command line
    '''
    p=argparse.ArgumentParser(description=('A simple random forest example'),formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument('--input', dest='namen', type=str,default='../data/dataRF.txt',help=('Input data table'))
    p.add_argument('--trainFrac', dest='trainFrac', type=float, default=0.7,help=('Fraction of data to use for training'))
    p.add_argument('--nTrees', dest='n_estimators', type=int, default=200,help=('Number of trees'))
    p.add_argument('--max_depth', dest='max_depth', type=int, default=None,help=('Maximum branch depth'))
    cmdargs=p.parse_args()
    return cmdargs


#################################################

class rfClass():
  '''Class to demonstrate random forest'''

  ##################

  def __init__(self,filename):
    '''Initialiser'''
    self.y,self.x1,self.x2,self.x3,self.x4=np.loadtxt(filename,usecols=(0,1,2,3,4),skiprows=1,unpack=True)

    # combine all x into one array with one column per feature variable. Solution found on stackoverflow
    self.x=np.column_stack((self.x1,self.x2,self.x3,self.x4))
    return


  ##################

  def splitData(self,trainFrac=0.7):
    '''Split into training and validation data'''

    self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.x,self.y,test_size=1-trainFrac,random_state=0)
    return


  ##################

  def buildRF(self,n_estimators,max_depth):
    '''Build a random forest model'''

    # initlise the class
    self.regressor=RandomForestRegressor(n_estimators=cmd.n_estimators,max_depth=cmd.max_depth,random_state=0)  # initialise the class

    # fit the model to the training data
    self.regressor.fit(self.x_train,self.y_train)           

    return

  ##################

  def predict(self):
    '''Predict the model on all the data'''

    self.y_pred=self.regressor.predict(self.x)  

    return



#################################################

if __name__=='__main__':
  '''Main block'''

  # read command line
  cmd=readCommands()

  # read the data into a class
  rfData=rfClass(cmd.namen)

  # try plotting it up to explore the behaviours?
  print('Add plotting code to this line')

  # spit into training and validation data
  rfData.splitData(cmd.trainFrac)

  # build the model
  rfData.buildRF(n_estimators=cmd.n_estimators,max_depth=cmd.max_depth)

  # predict the model on all the data
  rfData.predict()

  # validate the model using the validation data
  print('Add validation code here')


#################################################


