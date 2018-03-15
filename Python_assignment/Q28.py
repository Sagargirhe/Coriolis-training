#Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.
from functools import reduce
def find_longest_word(lis):
    return reduce(lambda x,y:x if len(x)>len(y) else y,lis)

print (find_longest_word(['sagar','suraj','suffiyan']))
