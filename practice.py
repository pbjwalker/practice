# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p173401
# sleep_in
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
  
# I'm not sure why this works yet. How does "or" work in a return statement?  How does python choose whether to return the boolean value of "not weekday" or to return "vacation"?  Maybe this is saying, "Return if this statement is True or False: it is not a weekday (not weekday) or vacation".
# Seems this:
#  return(vacation)
# means evaluate the statement, "vacation is True" and return if that statement is True or False
 

###################################

# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p197466
# diff21
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  value = abs(21 - n)
  if n>21:
    return value*2
  else:
    return value
    
# My solution worked correctly for all cases.
# Another solution provided by CodingBat approached it without using abs()

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

# Either way is just as good, I think.  Looks like it works out the same.

###################################











