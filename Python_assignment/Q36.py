'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.
'''
import re
from collections import defaultdict
def hapaxes(fname):
    d = defaultdict(int)
    f = open(fname,'r')
    hapx=[]
    w = f.read().lower()
    f.close()
    words = re.findall('\w+',w)
    for i in words:
        d[i]+=1
    for key in d:
        if d[key]==1:
            hapx.append(key)
    return hapx

#print (hapaxes('32.txt'))

