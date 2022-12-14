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

# CodingBat
# Logic-1 practice problems



