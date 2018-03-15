#Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.


def isVowel(c):
    V = ['a','e','i','o','u','A','E','I','O','U']
    return True if c in V else False

print (isVowel('o'))
