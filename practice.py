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

# My first solution used a for loop to iterate over the string, build a new string from the chars that are not index position n. It was very clunky and awkward.  Also, it's my understanding they wanted this done without loop, though I did it anyway.  I couldn't see how to do it without iterating over the string.  The code was so bad I didn't even copy it over here!

# Here's the CodingBat solution.  Oh, they used slicing!  That eliminates the need for iteration.  And there's no need to evaulate each char.  They give you the index position to exclude.

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
  
# I erased my code, re-did some of the other warmups, and tried it again.
# This is what I did the second time, with the new knowledge about slicing.  Basically the same thing as the official solution.

def missing_char(str, n):
  new_string = str[:n] + str[n+1::]
  return new_string

###################################

# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p120546
# monkey_trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

# Here's my solution:
def monkey_trouble(a_smile, b_smile):
  return ((a_smile and b_smile) or (not a_smile and not b_smile))

# I thought the task was straightforward.  It's helping me get more familiar with logic operations.

# Here's the solution provided by CodingBat:

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)
  
# I think that last line is brilliant!  Looking forward to this becoming second nature.

###################################

# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p166884
# parrot_trouble
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

# My solution:

def parrot_trouble(talking, hour):
  return((talking) and (hour < 7 or hour > 20))
  
# At first I had a logic error because I tried to do this:
# return((talking and hour < 7) and (talking and hour > 20))
# Once I fixed that error, it ran perfect.
# Got my second gold star for this one!!

# This was the solution from CodingBat:

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +
  
###################################

# Warmup-1
# Source: CodingBat
# https://codingbat.com/prob/p162058
# pos_neg
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

# my first try
def pos_neg(a, b, negative):
  if (negative and ((a < 0) and (b < 0))) or (not ((a > 0) and (b > 0))):
    return True
  else:
    return False


# my second try
def pos_neg(a, b, negative):
  if negative:
    if (a < 0) and (b < 0):
      return True
    else:
      return False
  else:
    if not ((a > 0) and (b > 0)):
      return True
    elif (a < 0) and (b < 0):
      return True
    else:
      return False

# my third try!
def pos_neg(a, b, negative):
  if negative:
    if (a < 0) and (b < 0):
      return True
    else:
      return False
  else:
    if (a < 0) and (b < 0):
      return False
    elif (a < 0) and (b < 0):
      return True
    else:
      return True

So close! Getting this logic right is not easy!

# my fourth try!!!
def pos_neg(a, b, negative):
  if negative:
    if (a < 0) and (b < 0):
      return True
    else:
      return False
  elif (a < 0) and (b < 0):
    return False
  elif (a > 0) and (b > 0):
    return False
  else:
      return True

# OK, finally got it. Got to be very careful with logic, for sure! My solution was really ugly and hard to read.
# Here's the CodingBat solution. It is so simple and streamlined!! Well, everyone starts somewhere. Practice, practice, practice.

def pos_neg(a, b, negative): if negative: return (a < 0 and b < 0) else: return ((a < 0 and b > 0) or (a > 0 and b < 0))

###################################

# Warmup-1
# Source: CodingBat





