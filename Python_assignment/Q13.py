#The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
import sys
def max_in_list(lis):
    m = -(sys.maxsize)
    for i in lis:
        m = i if i>m else m
    return m
print (max_in_list([43,23,545,65]))
