#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
import sys
def find_longest_word(lis):
    l = -(sys.maxsize)
    for i in lis:
        l=len(i) if len(i)>l else l
    return l
print (find_longest_word(['Coriolis','Technology']))

