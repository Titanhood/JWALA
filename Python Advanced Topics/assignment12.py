#question_1
list=[1,2,3,4,5,6,7,8]
New_List=[x**3 for x in list]
print(New_List)
#question_2
def prime(x):
    for i in range(2,x-1):
        if(x%i==0):
            return False
    else:
        return True
num=int(input("Starting Number "))
nume=int(input("Ending Number "))
lst=[]
for i in range(num,nume+1):
    lst.append(i)
primes=[i for i in lst if prime(i)]
print(primes)
#question_3
#List Comprehension
#Returns A List.
#Enclosed in []
#Takes More Size
#Can Access Elements by index.
#Generator Exppressons
#Returns a Generator Iterator which can be iterated over
#Enclosed in ()
#Takes Much Less Size
#Cannot Access Element By Index
