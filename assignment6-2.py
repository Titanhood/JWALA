#question_1
dict=eval(input('Enter value '))
print(dict)
for key in dict:
    print('key for the value {} is {}'.format(dict[key],key)) 
#question_2
d=dict()
marks=dict()
Mks=list()
Final=list()
n=int(input("students"))
for i in range (0,n):
    Name=input("Students Name ")
    Python=int(input("Marks in Python "))
    Java=int(input("Marks in Java "))
    Cpp=int(input("Marks in C++ "))
    D={'Name':Name.upper(),'Marks':{'Python':Python,'Java':Java,'C++':Cpp}}
    Final.append(D)
print(Final)
N_Find=input("Name of the student to find Marks ")
N_Find=N_Find.upper()
for i in range (0,len(Final)):
    if(N_Find==Final[i]['Name']):
        print("name of the student is : %s" %Final[i]['Name'])
        print("marks of the student in Python are : %d" %(Final[i]['Marks']['Python']))
        print("marks of the student in Java are : %d" %(Final[i]['Marks']['Java']))
        print("marks of the student in C++ are : %d" %(Final[i]['Marks']['C++']))
        break
    else:
        continue
else:
    print("Student Not Found")
