#define a class book with the following description
#data members
#bookname,book id,authorid,author name,price,book title
#member methods
#gatauthorid(),getauthorname(),getbooktitle(),getprice(),setauthorname(),
# setbooktitle(),setprice()

# class Book:
#     def __init__(self):
#         self.bname=input('enter bname')
#         self.bid=input('enter bid')
#         self.aid=input('enter aid')
#         self.aname=input('enter aname')
#         self.price=int(input('enter price'))
#         self.btitle=input('enter btitle')
#     def getauthorid(self):
#         print('aid is:',self.aid)
#     def getauthorname(self):
#         print('aname is:',self.aname)
#     def getbooktitle(self):
#         print('btitle is:',self.btitle)
#     def getprice(self):
#         print('price is:',self.price)
#     def setauthorname(self):
#         self.aname=input('enter new authornmae:')
#         self.getauthorname()
#     def setbooktitle(self):
#         self.btitle=input('enter new booktitle:')
#         self.getbooktitle()
#     def setprice(self):
#         self.price=int(input('enter new price'))
#         self.getprice()
# b=Book()
# b.setauthorname()
# b.setbooktitle()
# b.setprice()


#write a menu-driven python program for a banking system using a class
#account to perform the following operations:

#1.create  an account
#2.withdraw money
#3.deposit money
#4.display balance
#5.exit

#store account details in a list and search accounts using account number

#display 'account not found' if the account does not exist
#Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
# class Circle:
#     def __init__(self):
#         self.r=int(input("enter the radius of circle"))
#     def getarea(self):
#         self.area=3.14*self.r**2
#         print("area of circle:",self.area)
#     def getperimeter(self):
#         self.peri = 2*3.14*self.r
#         print("perimeter of circle:",self.peri)
# c=Circle()
# c.getarea()
# c.getperimeter()

#
# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

class Account:
    def __init__(self):
        self.accountno=int(input("enter acc no:"))
        self.accountname=input("enter account name:")
        self.balance=int(input("enter amount:"))
    def withdraw(self):
        self.amount = int(input("enter withdraw amount:"))
        self.balance-=self.amount
    def deposit(self):
        self.amount = int(input('enter deposit amount:'))
        self.balance+=self.amount
    def showbalance(self):
        print("current balance:",self.balance)
# b=Bank()
# b.withdraw()
# b.deposit()
# b.showbalace()
l=[]
while(1):
    print('manu-driven program')
    print('1.create an account')
    print('2.withdraw money')
    print('3.deposit money')
    print('4.display balance')
    print('5.exit')
    ch=int(input('enter your choice'))
    if ch==1:
        a=Account()
        l.append(a)
        #print(l)
    elif ch==2:
        num=int(input('enter the account number'))
        for i in l:
            if i.accountno==num:
                i.withdraw()
                break
            else:
                print('account not found')
    elif ch==3:
        num=int(input('enter the account number'))
        for i in l:
            if i.accountno==num:
                i.deposit()
                break
            else:
                print('account not found')
    elif ch==4:
        num=int(input('enter account number'))
        for i in l:
            if i.accountno==num:
                i.showbalance()
                break
            else:
                print('account not found')
    elif ch==5:
        exit()

