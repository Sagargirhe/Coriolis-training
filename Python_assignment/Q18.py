#A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

def is_pangram(string):
    s = set(string.lower())
    s.remove(' ')
    return True if len(s) == 26 else False

print (is_pangram('The quick brown fox jumps over the lazy dog'))
