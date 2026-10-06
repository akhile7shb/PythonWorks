#

# x=int(input("enter a numer:"))
# y=int(input("enter a numer:"))
# z=int(input("enter a numer:"))
# if(x>y and x>z):
#     print("first is larger")
# elif(y>z and y>x):
#     print("second larger")
# else:
#     print("third is larger")

#Write a program that asks the user for their age and prints whether they are a child, a teenager, or an adult.

age=int(input("enter the age"))
if age<=10:
    print("child")
elif age<=17:
    print("teenager")
else:
    print("adult")