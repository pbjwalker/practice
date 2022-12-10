# CodingBat
# https://codingbat.com/prob/p115413
# hello_name
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
# Here is my code:

def hello_name(name):
  return "Hello " + name + "!"

# Very easy, very quick
# My code is identical to thé solution

#############

# CodingBat
# make_abba
# https://codingbat.com/prob/p182144
# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
# Here's my code:

def make_abba(a, b):
  return a + b + b + a
  
# Their code is the same as mine, but without the parentheses.

###########

# CodingBat
# https://codingbat.com/prob/p132290
# make_tags
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


def make_tags(tag, word):
  return "<" +tag + ">" + word + "</" + tag +">"

# I got a gold star for this one
# No solution given

############

# CodingBat
# https://codingbat.com/prob/p129981
# make_out_word
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
# Here's my code:

def make_out_word(out, word):
  return out[:2] + word + out[2:]

# No solution provided

###############

# CodingBat
# https://codingbat.com/prob/p148853
# extra_end
# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
# Here's my code:

def extra_end(str):
  return (str[(len(str) - 2):] * 3)

# My first thought was to slice it from back to front.
# But I'm not sure that's possible.
# No solution provided

#############

# CodingBat







