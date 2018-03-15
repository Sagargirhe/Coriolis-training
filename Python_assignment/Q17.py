#Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def isPalindrome(phrase):
    m = []
    l = list(filter(lambda x: (x not in punctuations and x!= ' '),(list(map (lambda x:x.lower(),phrase)))))
    for i in reversed(l):
        m.append(i)
    return l==m


s = "Go hang a sala    mi I'm a lasagna hog."
print (isPalindrome(s))
