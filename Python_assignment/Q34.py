'''
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen. 
'''

from collections import defaultdict,OrderedDict
import sys
inFile = sys.argv[1]
def char_freq_table(fname):
    d = defaultdict(int)
    f = open(fname,'r')
    contents = f.read()
    for c in contents:
        d[c]+=1
    for k in OrderedDict(sorted(d.items())):
        if k != '\n':
            print (k+'     =      ',d[k])
char_freq_table(inFile) # Give Input File form terminal

