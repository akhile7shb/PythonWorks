#keyword

# def function(n,a):
#     print("name",n)
#     print("age",a)
# function(n="arun",a=30)

#default

# def fun(n,a=25):
#     print("name=",n)
#     print("age=",a)
# fun("arun",30)

# def greet(name="guest"):
#     print("hello,",name)
# greet("amal")
#
# def stud(name,mark=80):
#     print(name,'mark is', mark)
# stud("arun")


#arbitary

# def fun(*args):
#     print(args)
# fun(30,60)
# fun(1,2,3,4)
# fun(6,8,4,2)
#
# def fun(**kwargs):
#     print(kwargs)
# fun(name="arun",age=25)
# fun(name="adhi",age=21,place="alappy")
# fun(name="adhil",age=21,place="ekm",cousre="python")

#define a function that accepts any number of numbers and returns their sum

# def fun(*x):
#     sum=0
#     for i in x:
#         sum=sum+i
#     print(sum)
# fun(10,20,30)


def square(x):
    return x**2
result=square(4)
print(result)