#question_1
a=[1,2,3,4,5]
a=a[::-1]
print(a)
#question_2
import re
a= "HELLO! hello"
patterns= ['[A-Z]+']    
for p in patterns:
    match= re.findall(p, a)
    print(match)
#question_3
x=[]
y=int(input())
for i in range(y):
    z=int(input())
    x.append(z)
    print(x)
#question_4
a1=[1,2,3,2,1]
b1=a1[::-1]
if(a1==b1):
    print('palindrome')
else:
    print('not palindrome')
#question_5
import copy as c
list1=[1,2,3,4]
list2=c.deepcopy(list1)
print(list1)
list1[3]=75
print(list1)
print(list2)
#list 2 wont change because its a deep copy of list1
#A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
#A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.




