#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(lis,n):
    return list(filter(lambda x: len(x)>n,lis))

print (filter_long_words(['Coriolis','Technology'],9))
