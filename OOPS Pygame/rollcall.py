from random import *
class Person:
    def __init__(self, first, last, email, born):
        self.first = first
        self.last = last
        self.email = email
        self.born = born
    def info(self):
        print(self.first,self.last,self.email,self.born)
class Student(Person):
    def __init__(self, first, last, email, born,id,gpa):
        Person.__init__(self, first, last, email, born)
        self.id=id
        self.gpa=gpa
    def info(self):
        print(self.first,self.last,self.email,self.born,self.id,self.gpa)
class Teacher(Person):
    def __init__ (self,first,last,email,born,ids,classes,classsize):
        Person.__init__(self, first, last, email, born)
        self.ids=ids
        self.classes=classes
        self.classize=classsize
    def info(self):
        print(self.first,self.last)
        print()
        for c in self.classes:
            print(c.first,c.last,c.gpa,c.id)
class1=[]
class2=[]
class3=[]
names1=["Eric","Emma","Joe","Harry","Taylor","Tom","Zach"]
names2=["Johnson","Japson","Swarna, Peckleman","Joe","John","HIIIIII"]
email=["1234","1324","1432","4567","5678","8976","1250"]
ids=["123456","234567","345678","456789","567890","124356","123458"]
gpa=[4.0,3.8,2.9,3.0,3.4,3.5,0.0]
appendto=0
for x in range(0,3):
    appendto+=1
    for x in range(0,5):
        if appendto==1:
            class1.append(Student(names1[randint(0,5)],names2[randint(0,5)],
            email[randint(0,5)],1,ids[randint(0,5)],gpa[randint(0,5)]))
        if appendto==2:
            class2.append(Student(names1[randint(0,5)],names2[randint(0,5)],
            email[randint(0,5)],1,ids[randint(0,5)],gpa[randint(0,5)]))
        if appendto==3:
            class3.append(Student(names1[randint(0,5)],names2[randint(0,5)],
                email[randint(0,5)],1,ids[randint(0,5)],gpa[randint(0,5)]))
print()
teacher1=Teacher("Brandon","Coffey","BrandonCoffey.123456@gmail.com",1,"987654",class1,len(class1))
teacher2=Teacher("Jenny","Hoobler","JennyHoobler.123456@gmail.com",1,"986546",class2,len(class2))
teacher3=Teacher("Jeffery","Sherrat","JefferySherrat.123456@gmail.com",1,"125367",class1,len(class1))
teacher1.info()
print()
teacher2.info()
print()
teacher3.info()