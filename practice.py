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

# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p124676
# near_hundred
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
  return((abs(n-100)<=10) or (abs(n-200)<=10))


# My solution was nearly identical to the CodingBat solution:
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# And I got my first gold star on the site for that solution!

###################################

# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p149524
# missing_char
# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

# This was my solution.  It seems clunky.  Also, it's my understanding they wanted this done without loop.  How do you do it without a loop?

# Here's the CodingBat solution.  Oh, they used slicing!  That eliminates the need for iteration.  And there's no need to evaulate each char.  They give you the index position to exclude.

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
  





