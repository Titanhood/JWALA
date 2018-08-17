#question_1
a1=[input(),input(),input()]
print(a1)
#question_2
b1=['google','apple','facebook','microsoft','tesla']
c1=[a1+b1]
print(c1)
#question_3
calls=['alpha','romeo','beta','gamma']
a2=calls.count('alpha')
print(a2)
#question_4
a3=[12,23,73,14,25]
a3.sort()
print(a3)
#question_5
arr1=[12,23,73,14,25]
arr2=[13,24,75,18,32]
arr1.sort()
arr2.sort()
arr3=arr1+arr2
arr3.sort()
print(arr3)
#question_6
a=[1,2,3,4,5,6,7,8,9]
a_odd=0
a_even=0
for x in a:
    if not x%2:
        a_even+=1
    else:
        a_odd+=1
print('even',a_even)
print('odd',a_odd)


