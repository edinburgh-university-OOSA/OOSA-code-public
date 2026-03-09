


#############################
# An example of inheritance #
# and overloading           #
#############################

# import previous class definition and random number generator
import myBank
import random


# new classes, inheriting from yourBank

class evilBank(myBank.yourBank):
  '''Class to represent a bank that occasionally lies'''

  def inquiry(self):
    '''overload the inquiry operator to lie 50% of the time'''
    if(random.random()>0.5):
      return self.balance*1.2   # David M. Beazley, 2009
    else:
      return self.balance
 
