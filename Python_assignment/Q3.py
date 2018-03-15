#Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

def length(list1):
    cnt = 0 #initial count is zero
    for elem in list1:
        cnt+=1
    return cnt

l = [234,221,434,6,56,76,32]
print (length(l))
