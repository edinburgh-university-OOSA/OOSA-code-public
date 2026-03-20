########################################
# Script to run Random Forest to
# predict canopy height from Sentinel-2
# for real La Selva GEDI data.
# Euan Mitchell 2022   
########################################

import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde
from osgeo import gdal
from pyproj import Proj, transform
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import scipy.stats as sps
import osr
import argparse
import os
import glob

#######################################

# Defining the command line reading function
def readCommands():
    '''
    Read the arguments passed from the command line
    '''
    p=argparse.ArgumentParser(description=('Specify input ALS and GEDI data files and programme control'),
        formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument('--gedi', dest='gediName', type=str,\
              default='/geos/netdata/oosa/week5/randomForest/gediL2A/processed_GEDI02_A_2019227223906_O03821_03_T03112_02_003_01_V002.h5 ',help=('GEDI filename'))
    p.add_argument('--sentinel2', dest='s2name', type=str, default='/geos/netdata/oosa/week5/randomForest/sentinel2/laselva20mComposite.tif',help=('Sentinel-2 filename'))
    p.add_argument('--nTrees', dest='n_estimators', type=int, default=200,help=('Number of trees'))
    p.add_argument('--max_depth', dest='max_depth', type=int, default=None,help=('Maximum branch depth'))

    cmdargs=p.parse_args()
    return cmdargs


#######################################

class RandomForest():
    '''
    A class to read output of gediMetric, GEDI L2A files, and imagery rasters
    and implement the Random Forest algorithm.
    '''

    def __init__(self):
        '''Class initialiser. Does nothing except get the class ready'''
        return


    def readGedi(self,filename):
        '''Read the GEDI L2A file'''

        print('Reading GEDI data from', filename)

        beamlist=['BEAM0101','BEAM1000','BEAM0010','BEAM0000','BEAM0011','BEAM0110','BEAM0001','BEAM1011']

        # the commented out lines would allow a whole directory of data to be read
        #inputs='*.h5'
        #path=os.path.join(inDir,inputs)
        fileList=[filename] # glob.glob(path)

        # create empty arrays ready to hold the data
        self.shotNumb=np.empty(0,dtype=np.uint64)
        lowestMode=np.empty(0,dtype=float)
        rh95=np.empty(0,dtype=float)
        qualFlag=np.empty(0,dtype=float)
        ground1=np.empty(0,dtype=float)
        ground2=np.empty(0,dtype=float)
        ground3=np.empty(0,dtype=float)
        ground4=np.empty(0,dtype=float)
        ground5=np.empty(0,dtype=float)
        ground6=np.empty(0,dtype=float)
        self.lon=np.empty(0,dtype=float)
        self.lat=np.empty(0,dtype=float)


        # loop over multiple files
        for file in fileList:
            f=h5py.File(file,'r')
            for beam in beamlist:
                try:
                  # read data from the HDF5 file
                  self.shotNumb=np.append(self.shotNumb,f[beam]['shot_number'])
                  lowestMode=np.append(lowestMode,f[beam]['elev_lowestmode'])
                  rh95=np.append(rh95,f[beam]['rh'][:,95])
                  qualFlag=np.append(qualFlag,f[beam]['quality_flag'])
                  ground1=np.append(ground1,f[beam]['geolocation']['elev_lowestmode_a1'])
                  ground2=np.append(ground2,f[beam]['geolocation']['elev_lowestmode_a2'])
                  ground3=np.append(ground3,f[beam]['geolocation']['elev_lowestmode_a3'])
                  ground4=np.append(ground4,f[beam]['geolocation']['elev_lowestmode_a4'])
                  ground5=np.append(ground5,f[beam]['geolocation']['elev_lowestmode_a5'])
                  ground6=np.append(ground6,f[beam]['geolocation']['elev_lowestmode_a6'])
                  self.lon=np.append(self.lon,f[beam]['geolocation']['lon_lowestmode_a5'])     # cooordinates
                  self.lat=np.append(self.lat,f[beam]['geolocation']['lat_lowestmode_a5'])
                except:
                    print('Empty beam',beam)
                    continue

        # reproject gedi to sentinel-2
        inProj=Proj(init="epsg:4326")
        outProj=Proj(init="epsg:"+str(self.epsg))
        x,y=transform(inProj,outProj,self.lon,self.lat)
        self.lon=x
        self.lat=y
 
        self.gediData=np.stack((lowestMode,rh95,qualFlag,ground1,ground2,ground3,ground4,ground5,ground6),axis=1)
        self.nFootprints=self.gediData.shape[0]
        print('gediData shape',self.gediData.shape)
        return

    def readTiff(self,filename):
        '''Read in a sentinel-2 image as a combined geotiff'''

        # Read and process NDVI image
        ds=gdal.Open(filename)

        proj=osr.SpatialReference(wkt=ds.GetProjection())
        self.epsg=int(proj.GetAttrValue('Authority',1))
        self.nX=ds.RasterXSize
        self.nY=ds.RasterYSize

        # Get image origin and resolution info
        transform=ds.GetGeoTransform()
        self.xOrigin=transform[0]
        self.yOrigin=transform[3]
        self.xPixel=transform[1]
        self.yPixel=transform[5]

        # Read each raster band into 3D numpy array
        self.tiffData=ds.ReadAsArray(0,0,self.nX,self.nY)
        return


    def tiffExtract(self):
        '''Extract data from raster at footprint locations through vector-raster intersection'''

        self.tiffExtract=np.zeros((self.nFootprints,14))  # this is number of GEDI footprints * number of S2 bands
        self.gediExtract=np.zeros((self.nFootprints,9))
        print('tiffExtract shape',self.tiffExtract.shape)
        print('gediExtract shape',self.gediExtract.shape)

        # loop over GEDI footprints
        for i in range(self.nFootprints):

            xDist=self.lon[i]-self.xOrigin
            yDist=self.lat[i]-self.yOrigin

            xInd=int((self.lon[i]-self.xOrigin)//self.xPixel)
            yInd=int((self.lat[i]-self.yOrigin)//self.yPixel)

            # delete overhangs
            if((xInd>=0)&(xInd<self.nX)&(yInd>0)&(yInd<self.nY)):
              self.tiffExtract[i,:]=self.tiffData[:,yInd,xInd]
              self.gediExtract[i,:]=self.gediData[i,:]

        return


    def generateForest(self,split=0.7,n_estimators=200,max_depth=None):
        '''Run Random Forest algorithm with the imported datasets
           split is the fraction of data to use for model training
        '''

        plt.rcParams['figure.figsize']=(16,12)
        plt.rcParams['xtick.labelsize']=16
        plt.rcParams['ytick.labelsize']=16
        plt.rcParams['axes.labelsize']=18
        plt.rcParams['axes.labelpad']=8.0
        plt.rcParams['axes.titlesize']=20

        # Apply a quality_flag = 1 mask to the training data and define test data as the other data
        #self.train=np.where((self.gediExtract[:,2]==1.0))
        #self.test=np.where((self.gediExtract[:,2]==0.0))

        # Split into train and test datasets based on location instead
        #self.train=np.where(((self.use[:,8])<((self.use[:,7]*1.389)+6500)))
        #self.test=np.where((self.use[:,8])>((self.use[:,7]*1.389)+6500))

        # Split into train and test datasets randomly
        nTrain=int(split*self.nFootprints)
        rng=np.random.default_rng()
        self.train=rng.choice(self.nFootprints,size=nTrain,replace=False)
        self.test=np.empty((self.nFootprints-nTrain),dtype=int)
        j=0
        for i in range(0,self.nFootprints):
          if i not in self.train:
            self.test[j]=i
            j+=1

        #print('train length',len(self.train[0]))
        #print('test length',len(self.test[0]))

        #x=self.tiffExtract[self.train[0],:]
        #y=self.gediExtract[self.train[0],1]
        #x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=0)

        # Independent variables are Sentinel reflectances and indices
        x_train=self.tiffExtract[self.train,:]
        x_test=self.tiffExtract[self.test,:]
        print('Shape of x',x_train.shape)
        # Dependent variable is GEDI RH95
        y_train=self.gediExtract[self.train,1]
        y_test=self.gediExtract[self.test,1]
        print('Shape of y',y_train.shape)

        #plt.plot(x_train,y_train,'.')
        #plt.show()
        #plt.plot(x_test,y_test,'.')
        #plt.show()

        #for i in range(1,21):
        print('Running Random Forest algorithm ...')
        regressor=RandomForestRegressor(n_estimators=n_estimators,max_depth=max_depth,random_state=0)  # initialise the class
        print('Shapes',x_train.shape,y_train.shape)
        regressor.fit(x_train,y_train)           # train the random forest
        self.y_pred=regressor.predict(x_test)    # predict for test points

        # write out results
        print('y_pred shape',self.y_pred.shape)
        print('Random Forest coefficient',regressor.score(x_test,y_test))
        print('Random Forest MSE',mean_squared_error(y_test,self.y_pred))
        print('Random Forest RMSE',sqrt(mean_squared_error(y_test,self.y_pred)))
        print('Random Forest Bias',np.sum(self.y_pred-y_test)/self.y_pred.shape[0])
        #print('RF Feature Importance',regressor.feature_importances_)

        # Make canopy height map of RF model output
        '''plt.scatter(self.use[self.test[0],7],self.use[self.test[0],8],s=8,c=self.y_pred,cmap='Greens')
        plt.xlabel('Easting (m)')
        plt.ylabel('Northing (m)')
        plt.legend()
        plt.show()'''

        # Independently fit a linear regression to the RF output
        slope,intercept,r,p,se = sps.linregress(y_test,self.y_pred)
        print('Slope: {}, intercept: {}, r: {}, p: {}, std_err: {}'.format(slope,intercept,r,p,se))

        # Random Forest predicted canopy height versus GEDI L2A canopy height
        plt.plot(y_test,self.y_pred,'o',markersize=1)
        plt.plot([0,80], [0,80],ls='--',color='r')
        plt.xlim([0,80])
        plt.ylim([0,80])
        #plt.title('Random Forest Height Prediction')
        plt.xlabel('GEDI L2A RH95 (m)')
        plt.ylabel('RF Predicted Height (m)')
        graphName='realVsPred.png'
        plt.savefig('realVsPred.png',dpi=300)
        print('Graph drawn to',graphName)
        plt.close()
        plt.clf()

        # The difference between the RF prediction of canopy height and the GEDI L2A height value
        self.RFresidual=(self.y_pred-y_test)


#######################################

# The main block
if __name__ == '__main__':

    # read the command line
    args=readCommands()

    # read data, build model and assess accuracy
    comp=RandomForest()          # create an instance of the class that will handle the RF
    comp.readTiff(args.s2name)   # read sentinel-2 data into the class
    comp.readGedi(args.gediName) # read GEDI data into the class
    comp.tiffExtract()           # intersect the vector and raster data
    comp.generateForest(n_estimators=args.n_estimators,max_depth=args.max_depth)        # do the random forest

