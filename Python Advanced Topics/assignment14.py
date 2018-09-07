#question_1
def prime(x):
    for i in range(2,x-1):
        if(x%i==0):
            return False
    else:
        return True
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2=list(filter(prime,list1))
print(list2)
#question_2
from functools import reduce
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mul=reduce(lambda x,y:x*y,list1)
print(mul)
