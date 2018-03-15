#Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max1(n1,n2):
    return n1 if n1>n2 else n2

def max_of_three(n1,n2,n3):
    return max1(n1,n2) if max1(n1,n2) > n3 else n3

print (max_of_three(43,54,21))

