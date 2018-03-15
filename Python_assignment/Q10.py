#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
def overlapping(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    return False

print (overlapping([32,43,12,43],[31,21,423,32]))
