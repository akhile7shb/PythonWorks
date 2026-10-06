# def missing_number(l):
#     n_count=set()
#     for i in l:
#         if i not in n_count:
#             n_count.add(i)
#         else:
#             rep_num=i
#             print(f"Repeated number:{rep_num}")
#
#     for i in range(1,len(l)+1):
#         if i not in n_count:
#             miss_num=i
#             print(f"Missing number:{miss_num}")
#             break
#
#     return miss_num+rep_num
#
# num_list=[1,1,3,4]
# print(missing_number(num_list))

import math
def strong_number(n):
    s=str(n)
    sum=0
    for i in s:
        fact=math.factorial(int(i))
        sum=sum+fact
    if sum!=n:
        return False
    else:
        print(n,'strong number')
        return True
print(strong_number(145))


