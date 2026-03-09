

# base class for ASPRS .las point format 0.
class pointFormat0(object):
  # attribute definitions
  x=0
  y=0
  z=0
  # and all the others...

# class for ASPRS .las point format 1.
class pointFormat1(pointFormat0):
  # already contains all attributes of pointFormat0
  gpsTime=0

