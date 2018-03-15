#Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

from functools import reduce

def sum1(list1):
    return reduce(lambda x,y:x+y,list1)

def multiply(list1):
    return reduce(lambda x,y:x*y,list1)


l = [32,545,657,2,65,232]
print ("Sum is :",sum1(l))
print ("Multiplication is: ",multiply(l))
