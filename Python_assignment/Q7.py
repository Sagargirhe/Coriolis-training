#Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I"

def stringReversal(string):
    s = ""
    for i in string:
        s=i+s
    return s

print (stringReversal("I am testing"))

