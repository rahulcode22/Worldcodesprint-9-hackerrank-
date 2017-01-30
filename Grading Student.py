#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    # your code goes here
    y=(grade//5+1)*5
    diff=y-grade
    if diff<3 and (grade+diff)>=40:
        print grade+diff
    else:
        print grade
