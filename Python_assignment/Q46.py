'''
An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:

      "board": makes "bad" and "or".
      "waists": makes "wit" and "ass".

    Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion.
'''

def alternade(str0):
    str1 = ''
    str2 = ''
    n = len(str0) 
    for i in range(0,n,2):
        str1+=str0[i]
        if i+1>(n-1):
            break
        str2+=str0[i+1]
    return (str0,str1,str2)

f = open('Q46.txt','r')
lis = f.read().split('\n')
f.close()
l = list(map(lambda x:alternade(x),lis))
for i in l:
    if len(i[1]) > 1 and i[1] in lis and i[2] in lis:
        print ('"{0}": makes "{1}" and "{2}".'.format(i[0],i[1],i[2]))


