#question_1
pi=3.14
def area(r):
    ar = 4 * pi * r * r
    return ar
radius=int(input())
print('Area Of Sphere :',area(radius))
#question_2
def perfect(num):
    fact=[]
    sum=0
    for i in range (1,num-1):
        if(num%i==0):
            fact.append(i)
        else:
            continue
    for i in range(0,len(fact)):
        sum=sum+fact[i]
    if(sum==num):
        return True
    else:
        return False
perf=[] 
for i in range(1,1000):
    if(perfect(i)):
        perf.append(i)
print(perf)
#question_3
num=int(input())
for i in range(1, 11):
   print(num,'x',i,'=',num*i)
#question_4
def power(num,exp):
    if(exp==1):
        return(num)
    if(exp!=1):
        return(num*power(num,exp-1))
num=int(input("Enter num: "))
exp=int(input("Exponential value: "))
print("Result:",power(num,exp))
