#question_1
a=int(input())
if(a%4==0):
    print('Leap year')
else:
    print('Not a leap year')
#question_2
a=int(input())
b=int(input())
if(a==b):
    print('Sqaure')
else:
    print('Rectangle')
#question_3
a=list()
a.append(int(input('')))
a.append(int(input('')))
a.append(int(input('')))
t=set(a)
print(max(a))
print(min(a))
#question_4
sex=['M','F']
sex1=input('Enter sex ')
sex2=sex1.upper()
marital_status=input('Martial status')
age=int(input())
if(sex2 in sex):
    if(sex1=='M'):
        if(age>=20 and age<=40):
            print('work anywhere')
        elif(age>=40 and age<=60):
            print('Urban area only')
    else:
        print('Work in urban areas')
else:
    print('error')
#question_5
quantity=int(input('quantity '))
price=quantity*100
if(price>1000):
    print('With discount ',0.9*price)
else:
    print('Without discount ',price)
                                        #LOOPS
#question_1
a=[]
for i in range(0,10):
    num=int(input())
    a.append(num)
print('Numbers are: ')
for i in range(0,10):
    print(a[i])
#question_2
while True:
    print('a')
#question_3
x=[]
y=list()
for i in range (0,10):
    x.append(int(input('Enter Number ')))
    y.append(x[i]*x[i])
print('Square ')
for i in range (0,10):
    print(y[i])
#question_4
list1=[1,2,'hello',2.20]
list_int=list()
list_string=list()
list_float=list()
a=list()
for i in range(0,len(list1)):
    a.append(str(list1[i]))
for i in range(0,len(a)):
    if(a[i].isdigit()):
        list_int.append(int(a[i]))
    else:
        if(a[i].isalpha()):
            list_string.append(a[i])
        else:
            list_float.append(float(a[i]))
print('Float:-')
print(list_float)
print('The Integer Elements are :-')
print(list_int)
print('The String Elements are :-')
print(list_string)
#question_5
p=[]
p.append(1)
for i in range (2,100):
    for k in range(2,i-1):
        if(i%k==0):
            break
    else:
        prime.append(i)
prime.append(101)
print(prime)
#question_6
for i in range(1,5):
    print("*"*i)
#question_7
x1=list()
for i in range(0,10):
    num=input("Enter element")
    x1.append(num)
search=input("Delete")
for i in range(0,len(x1)-1):
    if(x1[i]==search):
        x1.remove(search)
else:
    print("Element not found")
print(x1)
         
