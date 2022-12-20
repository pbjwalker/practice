# CodingBat
# Logic-1 practice problems
# https://codingbat.com/prob/p195669
# cigar_party
# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
# Here's my code:

def cigar_party(cigars, is_weekend):
  if is_weekend and cigars>=40:
    return True
  elif cigars>=40 and cigars<=60:
    return True
  else:
    return False

# My solution worked, but I need more practice with logic problems.
# Here is the CodingBat solution.  It uses logic better than mine.

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

############
# CodingBat
# Logic-1 practice problems
# https://codingbat.com/prob/p129125
# date_fashion
# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
# Here's my code:

def date_fashion(you,date):
  if (you >= 8) or (date >= 8):
    return 2
  elif (you <= 2) or (date <= 2):
    return 0
  else:
    return 1

# My first run had an error.
# It didn't take into account the exception.
# Just needed to make the check on the exception first.
# Here's the fixed code:

def date_fashion(you,date):
  if (you <= 2) or (date <= 2):
    return 0
  elif (you >= 8) or (date >= 8):
    return 2
  else:
    return 1

# My code is identical to the solution.


############
# CodingBat
# Logic-1 practice problems
# https://codingbat.com/prob/p135815
# squirrel_play
# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
# Here's my code:

def squirrel_play(temp, is_summer):
  if is_summer:
    return (temp >= 60) and (temp <= 100)
  else:
    return (temp >= 60) and (temp <= 90)
    
# And it worked perfect!  I got a gold star for this one!
# Granted it's a simple problem,
# but I like working with logic.
# No CodingBat solution provided.

############
# CodingBat
# Logic-1 practice problems
# https://codingbat.com/prob/p137202
# caught_speeding
# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# Here's my code:

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed >= 86:
      return 2
    elif speed <= 65:
      return 0
    else:
      return 1
  else:
    if speed >= 81:
      return 2
    elif speed <= 60:
      return 0
    else:
      return 1   
      
# That worked!
# I think that's a lot of if-elif-else statements.
# Maybe I'll learn a better way of doing that soon.

############
# CodingBat
# Logic-1 practice problems






