#Implement the higher order functions map(), filter() and reduce(). (They are built-in but writing them yourself may be a good exercise.


def mymap(fun,lis):
    result = []
    for i in lis:
        result.append(fun(i))
    return result

def myfilter(fun,lis):
    result = []
    for i in lis:
        if fun(i):
            result.append(i)
    return result
def myreduce(fun,lis):
    result = lis[0]
    for i in lis[1:]:
        result = fun(result,i)
    return result

print (list(mymap(len,['dadad','dsfsffs'])))
print (myfilter(lambda x: x>5,[434,2,3,4]))
print (myreduce(lambda x,y: x if x > y else y,[323,435,6]))


