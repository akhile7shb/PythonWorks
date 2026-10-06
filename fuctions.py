#addition of two numbers
from itertools import product, count


# def addition():
#     "additon of 2 numbers"
#     num1 = int(input("enter a number"))
#     num2 = int(input("enter a number"))
#     sum = num1 + num2
#     print('sum', sum)
#     return
#
#
# addition()


#define a function to display a message "Hello Your name"

# def name():
#     "display a message"
#     name=int(input('enter a name')
#     print("hello"+name)
#     return
# name()

#define a function to print the factorial of a number

# def factorial():
#     "factorial of a number"
#     num=int(input("enter a number"))
#     for i in range(num-1,0,-1):
#         num*=i
#     print(num)
#     return
# factorial()

#define a function to find the number of occurence of a particular character in a string

# def occurence():
#     "occurence of a particular string"
#     num=input("enter a name")
#     ch=input("enter a character")
#     count=0
#     for i in num:
#      if i==ch:
#         count=count+1
#     print(count)
#     return
# occurence()


#define a function to print the sum of elements in a  list l=[89,45,67,12]
# l=[89,45,67,12]
# def add():
#     "sum of elements"
#     add=0
#     for i in l:
#         add=add+i
#     print(add)
#     return
#add()

#define a function whether a number is prime or not
#
# def prime(num):
#     "prime or not"
#     for i in range(2,num):
#         if num%i==0:
#          break
#     else:
#      return num
# result=prime(num=8)
# print(result,'is a prime number')


#define a function that takes 3 arguments(amount,rate,year)and find simple interest value

# def interest(p,n,r):
#     si=p*n*r/100
#     # print(si)
#     return si
# result=interest(2000,20,5)
# print(result)

#define a function that takes 3 numbers and returns the product of 3 numbers

# def  product(n1,n2,n3):
#     product=n1*n2*n3
#     print(product)
#     return product
# result=product(2,3,4)
# print(result)

#define a function that takes a string and a character and returns the number of occurence of the character in that string

# def occurence(string,ch):
#     count=0
#     for i in string:
#         if(i==ch):
#             count=count+1
#     return count
# result=occurence("arun",'a')
# print(result)


# def palindrome(x):
#     if(x[::-1]==x):
#      return x
# result=palindrome('mala')
# print(result)

#define a function that takes the list of argument and returns  a new list containing unique elements from yhe list
#l=[12,34,78,12,67,34,90,23]

# l=[12,34,78,12,67,34,90,23]
# def list(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# result=list(l)
# print(result)

#define a function that takes two list as arguments and print common elements

# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def list(l1,l2):
#     for i in l1:
#         if i in l2:
#             print(i)
# result=list(list1,list2)


# def factorial(n):
#     product=1
#     for i in range(n,1,-1):
#         product*=i
#     return product
# print(factorial(5))

# def multiple(n):
#     if n%2==0:
#      return n
# result=multiple(8)
# print(result)

# def occurence(string,ch):
#     count=0
#     for i in string:
#         if i==ch:
#             count+=1
#     print(count)
# occurence('amal','a')
# def fact(n):
#     product=1
#     for i in range(n,1,-1):
#         product*=i
#     return product
# print(fact(5))

# def palin(p):
#     if(p[::-1]==p):
#      return p
# print(palin('mala'))
#

# def product(n):
#     product=1
#     for i in range(n,1,-1):
# #         product*=i
# #     return product
# # print(product(6))
#
# def factorial():
#     num=int(input('enter number'))
#     for i in range(num-1,0,-1):
#         num*=i
#     print(num)
#     return
# factorial()

# def palin(s):
#     if(s[::-1]==s):
#         return s
# print(palin('malay'))

def occurence(string,ch):
    count=0
    for i in string:
        if i==ch:
            count+=1
        print(count)
occurence('arun','u')




