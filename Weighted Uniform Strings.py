import sys
from string import ascii_lowercase
from sets import Set
 
s = raw_input().strip()
n = int(raw_input().strip())
 
# Construct hash table of alphabet weights
weight = {}
current_letter = 1
for a in ascii_lowercase:
    weight[a] = current_letter
    current_letter += 1
 
# Set containing weights for all possible uniform substrings
U = Set()
 
character = s[0]
current_weight = 0
for i in range(len(s)):
    if s[i] == character:
        current_weight += weight[character]
    else:
        character = s[i]
        current_weight = weight[character]
    U.add(current_weight)
 
for a0 in xrange(n):
    x = int(raw_input().strip())
    # your code goes here
    if x in U:
        print "Yes"
    else:
        print "No"

