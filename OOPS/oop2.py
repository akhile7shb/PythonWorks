#define a class names employee with the following details
#data members
#Empid,name,age,salary,designation,place
#member functions
#getsalary(),showpersondetails()
#create two objects for the employee class and call the above member methods


class Employee():
    def __init__(self):
        self.empid=(input('enter the  id'))
        self.name=input('enter the name')
        self.age=int(input('enter the age'))
        self.salary=int(input('enter the salary'))
        self.designation=input('enter the designation')
        self.place=input('enter the place')
    def getsalary(self):
        print(self.empid,self.salary)
    def display(self):
        print('emp id:',self.empid,'name is:',self.name,'age is:',self.age,'designation is:',self.designation,'place is:',self.place)
e=Employee()
e.getsalary()
e.display()
e1=Employee()
e1.display()