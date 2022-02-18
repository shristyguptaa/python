# Class inside a class
class Person:
    def __init__ (self,id,name):
        self.id=id
        self.name=name
        self.db=self.DOB(1,11,2002)  #object

    def display(self):
        print("Id = ",self.id)
        print("Name = ",self.name)
        self.db.display()

    class DOB:
        def __init__(self,d,m,y):
            self.dd=d
            self.mm=m
            self.yy=y

        def display(self):
            print("DOB = {}/{}/{}".format(self.dd,self.mm,self.yy))

p1 = Person(1,"gg")
p1.display()
