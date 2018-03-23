#Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

from functools import reduce

def sum1(list1):
    s = 0
    for i in list1:
        s += i
    return s

def multiply(list1):
    m = 1
    for i in list1:
        m*=i
    return m

l = [32,545,657,2,65,232]
print ("Sum is :",sum1(l))
print ("Multiplication is: ",multiply(l))
