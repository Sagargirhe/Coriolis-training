#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(lis):
    return max(list(map(len,lis)))

print (find_longest_word(['Coriolis','Technology']))

