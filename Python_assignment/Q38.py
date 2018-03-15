#Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).

import re
from functools import reduce
def avg_word_len(fname):
    with open(fname,'r') as f:
        r = f.read()
        words = re.findall('\w+',r)
    return reduce(lambda x,y:x+y,list(map(len,words)))//len(words)

#print (avg_word_len('32.txt'))
