#Check whether a number is an Armstrong

# n=int(input("enter the number"))
# s=str(n)
# l=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**l
# if(sum==n):
#     print("amstrong")
# else:
#     print("not armstrong")

#Given a list
#l=[1,2,3,4]

# create a new list with squares of each element

# new=[]
# for i in l:
#     new.append(i**2)
# print(new)

#Given a list

#l=[12,67,59,23]

#create a list with elements whose value is greater than 50.
# new=[]
# for i in l:
#     if (i>50):
#         new.append(i)
# print(new)

# create a new set with elements whose value is greater than 50

# new=set()
# for i in l:
#     if (i>50):
#         new.add(i)
# print(new)


#Given a list
#
#l=[1,2,3,4]
#create a new dictionary where keys are numbers and values are squares of each number

# new={}
# for i in l:
#     new[i]=i**2
# print(new)

#create a list of 5 random numbers

# new=[]
# for i in range(5):
#     n=int(input('enter a number'))
#     new.append(n)
# print(new)



#Find the factors of a number

# num=int(input("enter the number "))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)

#find the fibinocci series


# a=0
# b=1
# for i in range(1,11):
#     print(a)
#     a,b=b,a+b



# for i in range(1,11):
#     if(i==7):
#         break
#     print(i)

# for i in range(1,26):
#     if(i==15):
#         break
#     print(i)
# else:
#     print("hello")

#write a program to check whether the number is prime or not

# num=int(input("enter the number"))
# for i in range(2,num):
#     if(num%i==0):
#         print("not prime")
#         break
# else:
#         print("prime")

# num=int(input("enter the number"))
# if(num>1):
#     for i in range(2,num):
#         if(num%i==0):
#             print("not prime")
#     else:
#         print("prime")
# else:
#     print("neither prime or composite")

#check whether a number is perfect or not

# num=int(input("enter the number"))
# sum=0
# for i in range(1,num):
#         if(num%i==0):
#             sum=sum+i
# if (sum==num):
#             print(num,"number is perfect")
# else:
#             print(num,"not perfect")
