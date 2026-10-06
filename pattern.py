#
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k**2,end=" ")
#         k=k+1
#     print()

# k=1
# for i in range(1,6,2):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,6,2):
#     for j in range(1,i+1):
#         if(j%2==0):
#           print('A',end=" ")
#         else:
#             print('1',end=" ")
#     print()

#       *
#     *   *
#   *   *   *
# *   *   *   *


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):#loop for adding extra space in each line
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end="   ")
#     print()

# *  *  *  *
#  *  *  *
#    *  *
#      *

# k=0
# for i in range(5,1,-1):
#     for p in range(k+1):#loop for adding extra space in each line
#         print("",end=" ")
#     k=k+2
#     for j in range(1,i):
#         print('*',end="   ")
#     print()



#      *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end="   ")
#     print()
#
# k=0
# for i in range(4,1,-1):
#     for p in range(k+2):
#         print("",end=" ")
#     k=k+2
#     for j in range(1,i):
#         print('*',end="   ")
#     print()
#

# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

# k=0
# for i in range(1,5):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# k=0
# for i in range(3,0,-1):
#     for p in range(k-1):
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

 #     * *
 #     * *
 #   * * * *
 #   * * * *
 #  * * * * * *
 #  * * * * * *
 # * * * * * * * *
 # * * * * * * * *

# k=6
# for i in range(2,9,2):
#     for l in range(2):
#         for p in range(1,k+2):
#             print("",end=" ")
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
#     k=k-2
#


# *
# **
# ***
# *****
# ******

# k=0
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#         k=k+1
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *


# k=3*2
# for i in range(5,0,-1):
#     for p in range(k-2):
#         print("",end="")
#         k=k-2
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#     *
#    ***
#   *****
#  *******
# *********

# k=5
# for i in range(1,11,2):
#     for p in range(1,k+1):
#      print("",end=" ")
#     k=k-1
#     for j in range(1,i+1):
#      print("*",end="")
#     print()


# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()

# for  i in range(1,11):
#     for j  in range(1,i+1):
#         print("*",end="")
#     print()


# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# k=5
# for i in range(1,k+1):
#     print(' ' *(k-i)+'* '*i)

k=5
for i in range(1,k+1):
    print(' ' *(k-i)+'* '*i)
for i in range(k-1,0,-1):
    print(' ' *(k-i)+'* '*i)

