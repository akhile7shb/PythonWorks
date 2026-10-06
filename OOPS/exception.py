#sum of two numbers
#
try:
    a=int(input('enter a number'))
    b=int(input('enter a number'))
    s=a/b
    print(s)
except ValueError:
     print('Value Error')
except ZeroDivisionError:
    print('Zero Division Error')
else:
    print('no exception in normal code')
finally:
    print('finished')

# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# import math
# try:
#     a=(int(input('enter a number')))
#     print(math.factorial(a))
# except ValueError:
#     print('value error')


# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

# try:
#     a=int(input('enter a number'))
#     b=int(input('enter a number'))
#     op=input('enter an operator')

#
#     if op=='+':
#         print(a+b)
#     elif op=='-':
#         print(a-b)
#     elif op=='*':
#         print(a*b)
#     elif op=='/':
#         print(a/b)
#     else:
#         print('invalid op')
# except ValueError:
#     print('value error')
# except ZeroDivisionError:
#     print('zero division')

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

# try:
#     file_name=int(input('file name'))


# import math
# try:
#     n=int(input('enter the number'))
#     f=math.factorial(n)
#     print(f)
# except Exception as a:
#     print(a)
#     print(type(a))
