class Person:
    def __init__(self):
        self.name=input('enter the name')
        self.age=input('enter your age')
    def showdetails(self):
        print('name:',self.name)
        print('age:',self.age)
class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno=int(input('enter the roll number:'))
    def studentdetails(self):
        super().showdetails()
        print('roll no:',self.rollno)
s=Student()
s.studentdetails()


# class Company:
#     def __init__(self):
#         self.cname=input('enter the company name:')
#     def showdetails(self):
#         print('company name:',self.cname)
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.empid=input('enter the employeeid')
#         self.designation=input('enter the designation')
#         self.salary=int(input('enter the salary'))
#     def getsalary(self):
#         print('salary is:',self.salary)
#     def showemployeedtails(self):
#         super().showdetails()
#         self.getsalary()
#         print('designation:',self.designation)
# e=Employee()
# e.showemployeedtails()
# e.getsalary()
#
