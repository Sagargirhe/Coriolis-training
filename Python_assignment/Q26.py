#Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?


from functools import reduce
def max_in_list(lis):
    return reduce(lambda x,y: x if x>y else y,lis)

print (max_in_list([42,43,23,76,99,1]))
