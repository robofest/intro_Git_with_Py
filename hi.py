# Simple program to introduce Git and GitHub
import sys
from big_HI import *

if len(sys.argv) == 1: # no command line arg
    n = 4
else:
    n = int(sys.argv[1])
for _ in range(n):
    #print('hi')
    display_big_HI()
