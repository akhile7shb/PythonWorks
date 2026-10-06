#define a class named person.accept name and age from the user.
#display the details by using show() method
#create an object and call the method

class Person:
    def __init__(self):
        self.name=input('enter the name')
        self.age=int(input('enter the age'))
    def show(self):
        print('name is:',self.name,'age is:',self.age)
p=Person()
p.show()
p1=Person()
p1.show()

