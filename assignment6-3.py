#question_1
class circle:
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        self.area=3.14*(self.rad**2)
        return self.area
    def circ(self):
        self.Cir=2*3.14*self.rad
        return self.Cir
rad=int(input("Enter Radius "))
c1=circle(rad)
print(c1.area())
print(c1.circ())
#question_2
class Student:
    def __init__(self,name,Rno):
        self.Name=name
        self.rno=Rno
    def setAge(self,age):
        self.Age=age
    def setMarks(self,marks):
        self.mark=marks
    def show(self):
        print("Name: {}".format(self.Name))
        print("Roll No: {}".format(self.rno))
        print("Age: {}".format(self.Age))
        print("Marks: {}".format(self.mark))
name=input("Name of the Student ")
rollno=int(input("RollNo of the Student "))
age=int(input("Age of the Student "))
marks=int(input("Marks of the Student "))

S1=Student(name,rollno)
S1.setAge(age)
S1.setMarks(marks)
S1.show()
#question_3
class temperature:
    def farh_to_celc(self, Cel):
        self.Celc = Cel
        self.Farh = ((self.Celc * 9) / 5) + 32
        print("Conversion ", self.Farh)
    def celc_to_farh(self, Farh):
        self.Farh = Farh
        self.Cel = (self.Farh - 32) * 5 / 9
        print("Conversion ",self.Cel)
choice = ['F', 'C']
T = temperature()
a = input("Input F for Converion to F and C for Conversion to C")
if a in choice:
    if a == 'F':
        cel = int(input("Enter Temprature in Celcius"))
        T.farh_to_celc(cel)
    else:
        far = int(input("Enter Temprature in Fahrenheit "))
        T.celc_to_farh(far)
else:
    print("PLease Enter Valid Input")
#question_4
class MovieDetails:
    Mov=list()
    def __init__(self,artist,release,rating):
        self.Aname=artist
        self.RelYear=release
        self.ratings=rating
    def Add(self):
        self.NewMov={'Artist':self.Aname,'Release Year':self.RelYear,'Ratings':self.ratings}
        self.Mov.append(self.NewMov)
    def Display(self):
        for i in range(0,len(self.Mov)):
            print("Artist {}".format(self.Mov[i]['Artist']))
            print("Release {}".format(self.Mov[i]['Release Year']))
            print("Ratings {}".format(self.Mov[i]['Ratings']))

BAAHUBALI=MovieDetails('PRABHAAS','2016','5')
BAAHUBALI.Add()
ROBOT=MovieDetails('RAJNI SIR','2014','4')
ROBOT.Add()
ROBOT.Display()
#question_5
class Animal:
    def animal_attribute(self):
        self.Color = 'Long Neck'
        self.legs = 4
        self.Food='Grass and Trees'
        print(self.Color, self.legs, self.Food, sep="\n")
class Tiger(Animal):
    def Yellow(self):
        pass
Tig = Tiger()
Tig.animal_attribute()
#question_6
A B
A B
#question_7
class Shape:
    __length=0
    __breadth=0
    def measurement(self):
        self.__length=int(input("Enter The Length Of the Shape "))
        self.__breadth=int(input("Enter The Breadth of the Shape "))
        return self.__length,self.__breadth
    def Area(self,leng,brd):
        self.Ar=leng*brd
        print(self.Ar)
class Rectangle(Shape):
    def __init__(self):
        pass
class Square(Shape):
    def __init__(self):
        pass

Sq=Square()
Rc=Rectangle()
sh=Shape()

ln,brd=sh.measurement()
if ln==brd:
    Sq.Area(ln,brd)
else:
    Rc.Area(ln,brd)

    















