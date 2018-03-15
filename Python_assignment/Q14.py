#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
def map_words_to_int(lis):
    l = list(map(len,lis))
    return l

print (map_words_to_int(['Coriolis','Technology']))
