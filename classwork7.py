# # # #Write a program to find the position of a character in a string

# s="hello world"
# print(s.index('l'))

# # # #write a program to find the count of character in  a string

#print(s.count('l'))

# # #create a random 5 digit otp number and print otp number

import random

from unicodedata import digit

# print(random.randrange(10000,99999))

# #create a list of  5 random 3 digit numbers

# new=[]
# for i in range(5):
#  new.append(random.randint(100,999))
# print(new)


# #create a dictionary where keys are words and values are length of each word from the string
#
#s="python coding is easy and fun"
# #
# # #new={'python':6,'coding':6,'is':2,'easy':4,'and':3,'fun':3}

# new={}
# for i in s.split():
#     new[i]=len(i)
# print(new)
#
# # # #create a dictionary where keys are each character and values are number of occurence of each character

#s="hello world"
#
# d={'h':1,'e':1,'l':3,'o':2,'':1,'w':1,'r':1,'d":1'}

# new={}
# for i in s:
#     new[i]=s.count(i)
# print(new)


# # #write a program to find the number of digits,letters,and spaces in a string
#
# s="sdfghjk3456789  dffghjkl345678"
# digitcount=0
# alphacount=0
# spacecount=0
# for i in s:
#     if i.isdigit():
#         digitcount+=1
#     elif i.isalpha():
#         alphacount+=1
#     elif i.isspace():
#         spacecount+=1
# print(digitcount)
# print(alphacount)
# print(spacecount)


# # Given a list

# l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]

# # # create a list of salaries

# salary=[i[2] for i in l]
# print(salary)


# # # find the maximum salary

# salary=[i[2] for i in l]
# print(max(salary))


# # # find minimum salary

# salary=[i[2] for i in l]
# print(min(salary))



#Given a dictionary
# d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
#
# # create a new list of students whose mark>=40
# new=[i for i ,mark in d.items() if mark>=40]
# print(new)

#Given two lists

l1=[11,27,34,45,56]
l2=[27,34,86,91]
#
# # Find Common elements
#
#
for i in l1:
    if i in l2:
     print(i)

#combine two list without duplicates
new=[]
for i in l1:
    if i in l2:
     new.append(i)
     print(i)

print(list(l1.union(l2)))


#Given

# l=[23,45,67,12,90,56]


#find second largest number
# l.sort(reverse=True)
# print(l[1])

#find second smallest number

# l.sort(reverse=True)
# print(l[4])


# d={'a':10,'b':20}
# for i,j in d.items():
#     print(i,j)