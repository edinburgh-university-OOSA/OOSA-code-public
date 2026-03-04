
'''
Three quotes (" or ') shows a document string. Use one
of these per functions, class and program.

The first one should contain the author, date and could 
explain licensing

S. Hancock    2021         Gnu Public License
'''

# Hashes can be used throughout the code to
# explain steps, break up colours and help
# to draw the eye

def someFunc():
  '''This is a function'''
  # it does not do much


################################

class someClass():
  '''This is a class'''
  # it also does little


# we can access the docu strings at runtime
print(help(someFunc))
print(someClass.__doc__)

