# l=["e","t","u"]
# l=' '.join('n')
# print(type(l))
#
# l=['n','u','p','t']
# l=tuple(l)
# print(type(l))
#
# l=['h','k','e','u']
# l=set(l)
# print(type(l))
#
# s=("python","pyshics","math")
# for i,s in enumerate(s):
#     print(i,s)


#
# n=int(input("enter the number:"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")
#
# n=int(input("enter the number:"))
# if n%2!=0:
#     print("prime")
# else:
#     print("not prime")


#
# n=int(input("enter the number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*2
# print("factorial number is:",n,"fact")

# fact=1
# n=int(input("enter the no:"))
# for i in range(1,n+1):
#     fact=fact*i
# print("fact",n,"is",fact)
# #
# a,b=0,1
# n=int(input("enter the number:"))
# print("febonessis series")
# print(" ",a," ",b,end="")
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print(" ",c,end="")

# Python program to illustrate the concept
# of threading
# importing the threading module

# n=int(input("enter no.:"))
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print("")
#
#
#
#
# for i in range(1,11):
#     print(i)



#
# n=4
# for i in range(1,n):
#     print(" ")
#     for j in range(i):
#         print(i,end=" ")
#     print(" ")


# def swaplist(newlist):
#
#     size=len(newlist)
#
#     temp=newlist[0]
#     newlist[0]=newlist[size-1]
#     newlist[size-1]=temp
#
#     return newlist
# newlist=[1,2,3,4,5]
# print(swaplist(newlist))
#
# def swap(newlist):
#     size=len(newlist)
#
#     temp=newlist
#     newlist=newlist
#     newlist=temp
#
#     return newlist
# newlist=[3,4]
# print(swaplist(newlist))
#
# n=len([1,2,3,4,5,3])
# print("length of list is:",n)
#
# n= len([10, 20, 30])
# print("The length of list is: ", n)
#
#
# list=['q','e','t']
# list.clear()
# print(list)
#
#
#
#
# lst=[ 1, 6, 3, 5, 3, 4 ]
# i=7
# if i in lst:
#     print("exist")
# else:
#     print("not exist")
#
#
# list=[ 1, 6, 3, 5, 3, 4 ]
# list.reverse()
# print(list)
#
# list1=[1,2,3,4,4]
# s= [i for i in list1]
# print(sum(s))
#
# def multi(list):
#     result = 1
#     for i in list:
#         result = result * i
#     return result
# list1=[1,2,3]
# list2=[2,3,4]
# print(multi(list1))
# print(multi(list2))
#
# l=[3,4,5,3]
# l.sort()
# print("smallest no list",l[0])
#
# l=[3,4,5,3]
# l.sort()
# print("largest no list",l[-1])
#
# l=[3,2,7,4,5,3]
# l.sort()
# print("largest no list",l[-2])
#
# l = [1000, 298, 3579, 100, 200, -45, 900]
# n = 4
# l.sort()
# print(l[-n:])
#
# list1 = [10, 21, 4, 45, 66, 93]
# for i in list1:
#     # checking condition
#     if i % 2 == 0:
#         print(i, end=" ")



# list1 = [10, 21, 4, 45, 66, 93]
# for i in list1:
#     # checking condition
#     if i % 2 != 0:
#         print(i, end=" ")


# list1=[-2,3,4,5,-4]
# for i  in list1:
#     if i >= 0:
#         print(i,end=" ")
#
# list1=[-2,-3,5,-6]
# for i in list1:
#     if i <= 0:
#         print(i,end=" ")

# test_list = [5, 6, [], 3, [], [], 9]
# print("The original list is : " + str(test_list))
# res = list(filter(None, test_list))
# print("List after empty list removal : " + str(res))



# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if i%5==0:
#             print("*",end=" ")
#         elif i%4==0:
#             print("#",end=" ")
#         elif i%3 ==0:
#             print("@",end=" ")
#         elif i %2==0:
#             print("!",end=" ")
#         else:
#             print("&",end=" ")
#     print()

# #
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if i>j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


#
# n=6
# for i in range(n):
#     for j in range(i+1):
#         if i<j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


#
# h=int(input("enter the height:"))
# b=int(input("enter the breath"))
# a=(h*b)/2
# print(a)



# n=int(input("enter the number"))
# p=(n**(0.5))
# print("the square root is",p)

#
# r=int(input("enter the radius"))
# a=3.14*r**2
# print(a)

a=int(input("enter the no"))
b=int(input("enter the no"))
if (a>b):
    min=a
else:
    min=b
while (1):
    if(min % a==0 and min % b==0):
         print("lcm",min)
         break
    min=min+1

