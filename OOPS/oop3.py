#Define a class named student with the following details
#Data members
#sname,rolllno,class,mark1,mark2,mark3
#member functions
#calculate(),calculate the total and average
#showdetails() display the details of a student with average mark
#create one object for the class and call the above member methods


# class Student:
#     def __init__(self):
#         self.name=input('enter the name')
#         self.rollno=int(input('enter the rollno'))
#         self.sclass=int(input('enter the class'))
#         self.mark1=int(input('enter the mark1'))
#         self.mark2=int(input('enter the mark2'))
#         self.mark3=int(input('enter the mark3'))
#     def calculate(self):
#          self.total=self.mark1+self.mark2+self.mark3
#          self.avg=self.total/3
#     def showdetails(self):
#          print('name is:',self.name,'roll no is:',self.rollno,'class is:',self.sclass,'total is:',self.total,'avg is:',self.avg)
# s=Student()
# s.calculate()
# s.showdetails()
class Student:
    def __init__(self,name,rollno,sclass,mark1,mark2,mark3):
        self.name=name
        self.rollno=rollno
        self.sclass=sclass
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def calculate(self):
        self.total = self.mark1 + self.mark2 + self.mark3
        self.avg=self.total/3
    def showdetails(self):
        print(self.name)
        print(self.rollno)
        print(self.sclass)
        print(self.mark1)
        print(self.mark2)
        print(self.mark3)
        print(self.total)
        print(self.avg)
e=Student(name="adhi",rollno=20,sclass=12,mark1=20,mark2=30,mark3=40)
e.calculate()
e.showdetails()