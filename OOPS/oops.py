#class Classname

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is:",self.name ,"age is:",self.age)
p=Person('arun',25)
p.display()
