
#########################
# An example of a class #
#########################

class yourBank(object):
  '''A demonstration of a class'''

  # an attribute to keep track of total number of accounts
  numb_accounts=0

  def __init__(self,name,balance):
    '''Class initialiser'''
    print("Creating a class")
    self.name=name
    self.balance=balance
    yourBank.numb_accounts+=1

  # methods
  def deposit(self,amt):
    '''Adds an amount of money'''
    self.balance=self.balance+amt

  def withdraw(self,amt):
    '''Removes an amount of money'''
    self.balance=self.balance-amt

  def inquiry(self):
    '''Returns the current balance'''
    return self.balance

