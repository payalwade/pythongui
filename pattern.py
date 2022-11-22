# n = 5
# for i in range(n):
#     for j in range(n, i, -1):
#         print("*", end="")
#     print()
#
# *****
#  ****
#   ***
#    **
#     *
#
# n = 5
# for i in range(n):
#     for j in range(n -i-1):
#         print(" ",end='')
#     for k in range(2*i+1):
#         print('*', end='')
#     print()
#     *
#    ***
#   *****
#  *******
# *********


# n = 5
# for i in range(n):
#     for j in range(i):
#         print(' ', end='')
#     for j in range(2*(n-i)-1):
#         print('*', end='')
#     print()
#
# *********
#  *******
#   *****
#    ***
#     *


# word="python"
# x=""
# for i in word:
#     x += i
#     print(x)


# for row in range(6):
#     for col in range(1,row+1):
#         print("*",end="  ")
#     print(" ")
#
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *

#
# for row in range(6):
#     for col in range(6,row,-1):
#         print("*",end="  ")
#     print(" ")
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *

# norow=int(input("enter the no:"))
# for row in range(1,norow):
#     for col in range(1,row+1):
#         print("{1}{1}".format(col,row),end=" ")
#     print()


# 11
# 22 22
# 33 33 33
# 44 44 44 44


# ch=64
# for row in range(1,norow):
#     for col in range(1,row+1):
#         ch=ch+1
#         print("{0}".format(chr(ch)),end=" ")
#     print()
#
#
# n=5
# for row in range(n,0,-1):
#     for col in range(1,row+1):
#         if row %2==0:
#             print("*",end="")
#         else:
#             print("#",end="")
#     print()
# #####
# ****
# ###
# **
# #

# array=[]
# n=int(input("how many no:"))
# for i in range(n):
#     number=int(input("enter no"))
#     array.append(number)
# print("maximum no is:",max(array))


# n=5
# for row in range(n,0,-1):
#     for col in range(1,row+1):
#         if row %5==0:
#             print("*",end="")
#         elif row%4==0:
#             print("#",end="")
#         elif row%3==0:
#             print("&",end="")
#         elif row%2==0:
#             print("$",end="")
#         else:
#             print("!",end="")
#     print()

# n= int(input("Enter the number of rows"))
# for i in range(n):
# 	for j in range(n-i-1):
# 		print("",end=" ")
# 	for k in  range(i+1):
# 		print("*", end=" ")
# 	print()
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# print("Inverted Full Pyramid of Stars (*): ")
# for i in range(5):
#     for s in range(i):
#         print(" ", end="")
#     for j in range(i, 5):
#         print("* ", end="")
#     print()


# * * * *
#  * * *
#   * *
#    *



# print("Pattern of Stars (*): ")
# k = 1
# for i in range(5):
#     for j in range(k):
#         print("* ", end="")
#     k = k + 2
#     print()
# *
# * * *
# * * * * *
# * * * * * * *
# * * * * * * * * *

# print("Pattern of Stars (*): ")
# k = 1
# space = 16
# for i in range(5):
#     for j in range(space):
#         print(" ", end="")
#     space = space-4
#     for j in range(k):
#         print("* ", end="")
#     k = k + 2
#     print()
#
#                 *
#             * * *
#         * * * * *
#     * * * * * * *
# * * * * * * * * *

#
# rowNum = 5
# space = rowNum-1
# for i in range(1, rowNum+1):
#   for j in range(1, space+1):
#     print(end=" ")
#   space = space-1
#   for j in range(2*i-1):
#     print(end="*")
#   print()
# space = 1
# for i in range(1, rowNum):
#   for j in range(1, space+1):
#     print(end=" ")
#   space = space+1
#   for j in range(1, 2*(rowNum-i)):
#     print(end="*")
#   print()
# n=int(input("enter the no"))
# for i in range(0,n):
#     for j in range(0,n):
#         if i==0 or j==(n-1) or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=int(input("enter the no"))
# for i in range(0,n):
#     for j in range(0,n):
#         if j==0 or i==(n-1) or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# *
# * *
# *   *
# *     *
# * * * * *


# n=int(input("enter the no"))
# for i in range(1,5):
#     for j in range(1,8):
#         if i==4 or i+j==5 or j-i==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#       *
#     *   *
#   *       *
# * * * * * * *
#
# #n=int(input("enter the no"))
# for i in range(0,5):
#     for j in range(0,5):
#         if i+j==2 or j-i==2 or i-j==2 or i+j==6 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     *
#   *   *
# *       *
#   *   *
#      *
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#
# for row in range(6):
#     for col in range(1,row+1):
#         print("*",end="  ")
#     print(" ")
# for row in range(6):
#     for col in range(6,row,-1):
#         print("*",end="  ")
#     print(" ")