# n=5
# for i in range(n):
#      for j in range(i+1):
#          print("*",end=" ")
#      print()
#
# *
# * *
# * * *
# * * * *
# * * * * *

#
# n=5
# for i in range(n):
#     for j in range(n,i,-1):
#         print("*",end=" ")
#     print()
#
# * * * * *
# * * * *
# * * *
# * *
# *


# n=6
# for i in range(n):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for z in range(0,i):
#         print("*",end="")
#     print()
#
# n=6
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for z in range(0,i):
#         print("*",end="")
#     print()


# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
#
# n=5
# for i in range(n):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for k in range(0,i):
#         print("*",end=" ")
#     print()

 #    *
 #   * *
 #  * * *
 # * * * *



# n=5
# for i in range(n):
#     for j in range(n,i,-1):
#         print(" ",end=" ")
#     for k in range(3*i+1):
#         print("*",end=" ")
#     print()
#
#           *
#         * * * *
#       * * * * * * *
#     * * * * * * * * * *
#   * * * * * * * * * * * * *

#
# n=5
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print("",end=" ")
#     for k in range(0,i):
#         print("*",end=" ")
#     print()
#
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# n=5
# for i in range(n):
#     for j in range(1,n+1):
#         if i==2 or j==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
#
#     *
#     *
# * * * * *
#     *
#     *

# n=5
# for i in range(n):
#     for j in range(n):
#         if ((i==0 or i==4) or (j==0 or j==4)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
#
# * * * * *
# *       *
# *       *
# *       *
# * * * * *



# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (j==1 or i==j or i==n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# *
# * *
# *   *
# *     *
# * * * * *


# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (j==n or i==n or j == n-i+1 ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
#         *
#       * *
#     *   *
#   *     *
# * * * * *


# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if  (i==j or j==n or i ==1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
#
# * * * * *
#   *     *
#     *   *
#       * *
#         *

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if i%5==0:
#             print("*",end=" ")
#         elif i%4==0:
#             print("#",end=" ")
#         elif i%3==0:
#             print("!",end=" ")
#         elif i%2==0:
#             print("^",end=" ")
#         else:
#             print("&",end=" ")
#     print()

#
# n=5
# for i in range(n):
#     for j in range(i+1):
#         if j%5==0:
#             print("*",end=" ")
#         elif j % 4 == 0:
#             print("#",end=" ")
#         elif j%3==0:
#             print("!",end=" ")
#         elif j%2==0:
#             print("^",end=" ")
#         else:
#             print("&",end=" ")
#     print()

# *
# * &
# * & ^
# * & ^ !
# * & ^ ! #
#
# rows = int(input("Enter number of rows: "))
# ascii_value = 65
# for i in range(rows):
#     for j in range(i + 1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")
#     ascii_value += 1
#     print("\n")
#
# a
# bb
# ccc
# dddd
#
# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     for j in range(i + 1):
#         print(j+1, end=" ")
#     print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     for j in range(i + 1):
#         print(i+1, end=" ")
#     print()
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# rows = int(input("Enter number of rows: "))
# number = 1
# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print(number, end=" ")
#         number += 1
#     print()
#
# Enter number of rows: 5
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

