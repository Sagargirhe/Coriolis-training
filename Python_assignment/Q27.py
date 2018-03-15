#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.

def words_to_int1(lis):
    l = []
    for i in lis:
        l.append(len(i))
    return l
def words_to_int2(lis):
    return list(map(len,lis))

def words_to_int3(lis):
    return [len(i) for i in lis]

print (words_to_int1(['safsd','asaf']))
print (words_to_int2(['safsd','asaf']))
print (words_to_int3(['safsd','asaf']))
