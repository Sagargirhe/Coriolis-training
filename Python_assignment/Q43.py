'''
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.
'''

from collections import defaultdict

def find_most_common_chars(lis):
    d = defaultdict(int)
    mx = 0
    l = []
    s = []
    for word in lis:
        str1 = ''.join(list(sorted(word)))
        d[str1]+=1
    for k in d:
        if mx<d[k]:
            mx=d[k]
            l = k
    for w in lis:
        if ''.join(list(sorted(w))) == l:
            s.append(w)
    return s

f = open('Q43.txt','r')
lis = f.read().split('\n')
f.close()
print (set(find_most_common_chars(lis)))


