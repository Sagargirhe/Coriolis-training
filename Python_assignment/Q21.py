#Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
from collections import defaultdict

def char_freq(string):
    d = defaultdict(int)
    for i in string:
        d[i]+=1
    return d

print (char_freq("abbabcbdbabdbdbabbbabcbcbab"))

