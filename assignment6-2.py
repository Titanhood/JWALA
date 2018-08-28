<<<<<<< HEAD
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
    Python=int(input("Marks in abc "))
    Java=int(input("Marks in xyz "))
    Cpp=int(input("Marks in pqr "))
    D={'Name':Name.upper(),'Marks':{'abc':Python,'xyz':Java,'pqr':Cpp}}
    Final.append(D)
print(Final)
N_Find=input("Name of the student to find Marks ")
N_Find=N_Find.upper()
for i in range (0,len(Final)):
    if(N_Find==Final[i]['Name']):
        print("name of the student is : %s" %Final[i]['Name'])
        print("marks of the student in abc are : %d" %(Final[i]['Marks']['abc']))
        print("marks of the student in xyz are : %d" %(Final[i]['Marks']['xyz']))
        print("marks of the student in pqr are : %d" %(Final[i]['Marks']['pqr']))
        break
    else:
        continue
else:
    print("Student Not Found")
=======
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
    Python=int(input("Marks in abc "))
    Java=int(input("Marks in xyz "))
    Cpp=int(input("Marks in pqr "))
    D={'Name':Name.upper(),'Marks':{'abc':Python,'xyz':Java,'pqr':Cpp}}
    Final.append(D)
print(Final)
N_Find=input("Name of the student to find Marks ")
N_Find=N_Find.upper()
for i in range (0,len(Final)):
    if(N_Find==Final[i]['Name']):
        print("name of the student is : %s" %Final[i]['Name'])
        print("marks of the student in abc are : %d" %(Final[i]['Marks']['abc']))
        print("marks of the student in xyz are : %d" %(Final[i]['Marks']['xyz']))
        print("marks of the student in pqr are : %d" %(Final[i]['Marks']['pqr']))
        break
    else:
        continue
else:
    print("Student Not Found")
>>>>>>> bfc3136c57691ea7819b922d050eafb8166273dd
