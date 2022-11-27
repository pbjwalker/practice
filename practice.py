# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p173401

# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

# This was my solution:

def sleep_in(weekday, vacation):
  if (weekday is False) or (vacation is True):
    return True
  else:
    return False
    
# A cleaner way to do it (and the official solution) was:

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
    
# "if not weekday" checks if weekday is False
# "if vacation" checks if vacation is True
# the "not" only applys to weekday

# A much shorter version also given by CodingBat is:

def sleep_in(weekday, vacation):
  return(not weekday or vacation)
  
# I'm not sure why this works yet. How does "or" work in a return statement?  How does python choose whether to return the boolean value of "not weekday" or to return "vacation"?


