'''
Your task in this exercise is as follows:

    Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
    Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.

Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
'''
import random
def generate_string(n):
    str1 = ''
    for i in range(n):
        str1+=random.choice(['[',']'])
    return str1
def check_balance(str1):
    stack = []
    i = 1
    for st in str1:
        if stack != [] and stack[-1] == '[' and st == ']':
            stack.pop()
        else:
            stack.append(st)
    return "OK" if stack == [] else "NOT OK"
print ('Enter the number to generate string:')
n = 2*int(input())
s = generate_string(n)
print (s,check_balance(s))

