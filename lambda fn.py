#lambda
# square=lambda x:x**2
# print(square(4))
#
# #cube of a number
#
# cube=lambda x:x**3
# print(cube(8))

#square root of  a number

# sqr=lambda x:x**0.5
# print(sqr(9))
#
# #length of a string
#
# s=lambda x:len(x)
# print(s("hello world"))
#
# #name attribute of a dictionary
#
# d=lambda x:x['name']
# print(d({'name':'arun'}))
#
# #first character of a string
#
# ch=lambda x:x[0]
# print(ch('hello'))
#
# #last element of a list
#
# l=lambda x:x[-1]
# print(l([12,3,4,56,78,8]))
#
# #sum of 2 numbers
#
# sum=lambda x,y:x+y
# print(sum(12,12))
#
# #sum of three numbers
#
# sum1=lambda x,y,z:x+y+z
# print(sum1(10,20,30))
#
# #product of 4 numbers
#
# product=lambda a,b,c,d:a*b*c*d
# print(product(2,3,4,5))

#higher order function

#map()

#create a list with squares of each number

# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))



#create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))

#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))


#create a new list of lengths

# colors=['red','green','blue','yellow','black']
#
# print(list(map(lambda x:len(x),colors)))
#
# #create a new list of first characters
#
# print(list(map(lambda x:x[0],colors)))

#create a new list of last characters

# print(list(map(lambda x:x[-1],colors)))
#
# #create a new list of reverse of each element
#
# print(list(map(lambda x:x[::-1],colors)))

#Given a list
# l=[23,78,12,56]
# Add 10 to each element in the given sequence

# print(list(map(lambda x:x+10,l)))

##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # create a new list of emails

# print(list(map(lambda x:x['email'],l)))


#filter

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))

#given a list
# l=[23,67,90,12,45,52]
# print(list(filter(lambda x:x>50,l)))
#

#given a list of fruits
# f=['apple','orange','grapes','pineapple','grapes']
# #fruits whose length is greater than  5
#
# print(list(filter(lambda x:len(x)>5,f)))

#given a list
#
# l=[34,78,96,23,12,15]
# #number divisible b 3 and 5
# print(list(filter(lambda x:x%3==0 and x%5==0,l)))
#
# #reduce
#
# l=[1,2,3,4]
# import functools
# print(functools.reduce(lambda a,b:a+b,l,0))
# print(functools.reduce(lambda a,b:a*b,l,1))
#
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
        print('names is:',self.name)
        print('roll no:',self.rollno)
        print(self.sclass)
        print(self.mark1)
        print(self.mark2)
        print(self.mark3)
        print(self.total)
        print(self.avg)
e=Student(name="adhi",rollno=20,sclass=12,mark1=20,mark2=30,mark3=40)
e.calculate()
e.showdetails()
