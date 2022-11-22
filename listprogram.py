# l=[2,5,6,5,7,2,1,8,6]
# d=[]
# for i in l:
#     if i not in d:
#         d.append(i)
#     else:
#         print(i,end=' ')

# l=[2,3,9,7,8]
# i=l.index(9)
# print(i)

# l=[2,'a',8,5,'r']
# for i in l:
#     if (type(i)==str):
#         print(i,end=" ")

# l=[2,'a',8,5,'r']
# for i in l:
#     if (type(i)==int):
#         print(i,end=" ")

# l1=[4,5,6,7]
# l2=[6,3,2,9]

# for i in l1:
#     for i in l2:
#         l2.remove(i)
#         print(i,end=" ")

# l1=[4,5,6,7]
# l2=[6,3,2,9]
# l1.reverse()
# l2.reverse()
# print(l1)
# print(l2)


# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

# list1 = [100, 200, 300, 400, 500]
# list1 = list1[::-2]
# print(list1)

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = [list1 + list2 for list1, list2 in zip(list1, list2)]
# print(list3)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for i in numbers:
#     res.append(i * i)
# print(res)

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res = [x + y for x in list1 for y in list2]
# print(res)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

# list1 = [5, 20, 15, 20, 25, 50, 20]
#
# while 20 in list1:
#     list1.remove(20)
# print(list1)

# a=[]
# n=int(input("enter the no. of element:"))
# for i in range(1,n+1):
#     b=int(input("enter no:"))
#     a.append(b)
# a.sort()
# print("largest no:",a[n-1])


# l=['m','k','i','k']
# l.append('k')
# print(l)
#
#
# l=['b','h','b']
# l.clear()
# print(l)
#
# l=['n','n','l','y']
# l.copy()
# print(l)
#
# l=['v','j','h','d']
# l.sort()
# print(l)

# l=['n','b','g','n']
# x=l.count('n')
# print(x)


# l=['k','l','f','u']
# m=['j','h','b']
# l.extend(m)
# print(l)

# l=['k','j','k']
# x=l.index('k')
# print(x)

# l=['k','l','j']
# l.insert(3,'m')
# print(l)

# l=['o','k','l']
# l.pop(2)
# print(l)

# l=['s','d','f']
# l.remove('d')
# print(l)

# l=['l','d','r','e']
# l.reverse()
# print(l)

# l=['e','r','t','y']
# l.sort()
# print(l)

# l=['e','r','t','y','i']
# l=l[::5]
# print(l)

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


# num=1234
# print(type(num))
# int_str=str(num)
# print(type(int_str))
#
# l=['y','y','e']
# print(type(l))
# l1=tuple(l)
# print(type(l1))
#
# set={"patl","bxdrtyj"}
# print(type(set))
#
#
# dec=dict.fromkeys(set)
# print(type(dec))
#
# u=set()
# print(type(u))
#
# l=[]
# print(type(l))
#
# l=()
# print(type(l))
#
# l={}
# print(type(l))
#
#
#
# my = ("a", "b", "a", "c", "c")
# # mylist = list(dict.fromkeys(mylist))
# # print(mylist)
# myw=tuple(set(my))
# print(myw)
#
# l=[2,33,222,14,25]
# m=l[4:]
# print(m)

# l=[1,2,3,4,4,5,6,7,4,5,2,7]
# m=set(l)
# # print(m)
# list=[1,2,6,'r',5,'u']
# for ele in list:
#     if (type(ele)==str):
#         print(ele)
#
# l1=[2,3,4,1,4]
# l2=[2,3,8,7,9]
# new=set(l1)-set(l2)
# l=l1+list(new)
# print(l)
#
# l=[2,5,7,3,9]
# l.insert(4,6)
# print(l)
#
# l=[2,5,7,3,9]
# l.pop(1)
# print(l)

# l=[2,5,7,3,9]
# l.append([4,3])
# print(l)
#
# l=[2,5,7,3,9]
# l.extend([3,9])
# print(l)

# l=[2,5,7,3,9]
# l1=l[:-1]
# print(l1)

# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# p=dict(zip(name, animal))
# print(p)

#
# p=list(range(5,10))
# print(list)
# print(p)

# stack = []
# stack.append('Jess')
# stack.append('Todd')
# stack.append('Yuan')
# print(stack) #=> ['Jess', 'Todd', 'Yuan']
# print(stack.pop()) #=> Yuan
# print(stack) #=> ['Jess', 'Todd']

#
# def bs(a):
#     b = len(a) - 1
#     # minus 1 because we always compare 2 adjacent values
#     for x in range(b):
#         for y in range(b - x):
#             a[y] = a[y + 1]
#
#     a = [32, 5, 3, 6, 7, 54, 87]
#     bs(a)


# list = ["1", "4", "0", "6", "9"]
# list = [int(i) for i in list]
# list.sort()
# print (list)

# mylist = []
# print("Enter 5 elements for the list: ")
# for i in range(5):
#     val = int(input("enter the number"))
#     mylist.append(val)
#
# print("Enter an element to be search: ")
# elem = int(input())
#
# for i in range(5):
#     if elem == mylist[i]:
#         print("\nElement found at Index:", i)
#         print("Element found at Position:", i+1)

