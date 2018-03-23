#According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

import re
def revstr(st):
    s =''
    for i in st:
        s = i+s
    return s
def semordnilap_recogniser(fname):
    semdlp = []
    f = open(fname,'r')
    st = f.read()
    newstr = re.sub('\ +',' ',st)
    newstr = re.sub('\n',' ',st)
    newstr1 = newstr.split(' ')
    for i in range(len(newstr1)-1):
            if revstr(newstr1[i]) in (newstr1[0:i]+newstr1[i+1:]):
                semdlp.append((newstr1[i]+' '+revstr(newstr1[i])))
    f.close()
    return semdlp

print (semordnilap_recogniser('Q33.txt'))
