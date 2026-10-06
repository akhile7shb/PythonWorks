#write a program to find the maximum number in a list


# l=[23,78,45,70,12,56]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
#         print(max)

# min=l[0]
# for i in l:
#     if i<min:
#         min=i
#         print(min)


# n=int(input('enter the number'))
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b\


# for i in range(5):
#     for j in range(5,i,-1):
#         print(j,end=" ")
#     print()


# for i in range(1,101):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         print(i,end="")

# def strong(n):
#     import math
#     s=str(n)
#     sum=0
#     for i in s:
#         fact=math.factorial(int(i))
#         sum=sum+fact
#     if sum!=n:
#         return False
#     else:
#         print(n,'strong number')
#         return True
# print(strong(145))

# l=[0,1,0,3,12]
#
# new_list=sorted(l,key=lambda x:x==0)
# print(new_list)

# employees=[ {"name": "arun", "age": 20, "email": "arun@gmail.com"},
#             {"name": "abhi", "age": 24, "email": "abhi@gmail.com"},
#             {"name": "amal", "age": 25, "email": "amal@gmail.com"}]
# emails=list(map(lambda x:x["email"],employees))
# print(emails)
class Employee:

    def __init__(self,i_d,name,age,designation,experience,salary):

        self.i_d=i_d

        self.name=name

        self.age=age

        self.designation=designation

        self.experience=experience

        self.salary=salary



    def employee_details(self):

        print(self.i_d)

        print(self.name)

        print(self.age)

        print(self.designation)

        print(self.experience)

        print(self.salary)



    def update(self,new_d):

        self.designation=new_d

        print('newdesignation:',self.designation)



    def promotion(self):

        if(self.experience>5 and self.age>30):

            print('promotion eligible')



        else:

            print('not eligible for promotion')



e=Employee(i_d=1,name='anu',age=23,designation='developer',experience=6,salary='50000')

e.employee_details()

e.update(new_d='manager')
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

e.promotion()

