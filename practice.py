# fibonacci series
# a=0
# b=1
# n=int(input("enter the no:"))
# print("fibonacci series")
# print(" ",a," ",b,end=" ")
# for i in range(n):
#      c=a+b
#      a=b
#      b=c
#      print(" ",c,end="")

# how to find avareage of n number in python
# num = int(input("How many numbers:-"))
# total_sum=0
# for n in range(num):
#     numbers=int(input("enter any no:"))
#     total_sum+=numbers
# avg=total_sum/num
# print("Average is:",avg)


#surface of area sphear
# PI = 3.14
# radius = float(input('Please Enter the Radius of a Sphere: '))
# sa =  4 * PI * radius * radius
# Volume = (4 / 3) * PI * radius * radius * radius
# print("The Surface area of a Sphere = %.2f" %sa)
# print("The Volume of a Sphere = %.2f" %Volume)


# find area of circle
# r=int(input("enter no:"))
# a=3.14*r**2
# print("area of circle:",a)


# a=float(input("enter no1:"))
# b=float(input("enter no2:"))
# c=float(input("enter no3:"))
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print('area of circle:',area)

# find of area of triangle
# b=int(input("enter breadth"))
# h=int(input("enter height"))
# area=(b*h)/2
# print("area of triangle:",area)


# find the even or odd
# n=int(input("enter the number:-"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

# find the prime or not prime
# n=int(input("enter the number:-"))
# if n%2!=0:
#     print("prime")
# else:
#     print("not prime")

# swap of two number
# a=int(input("enter no. a:"))
# b=int(input("enter no. b:"))
# temp=a
# a=b
# b=temp
# print("a=",a,"b=",b)


# find the factorial
# fact=1
# n=int(input("enter the no.:-"))
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial:",fact)

# find perfect number
# num=int(input("enter the no:"))
# sum=0
# for i in range(1,num):
#     if(num % i== 0):
#         sum=sum+i
# if sum==num:
#     print("perfect no")
# else:
#     print("not perfect")

# Armstrong number
# num = int(input("Enter 3-digit number : "))
# sum = 0
# temp = num
# # Define a function
# while temp > 0:
#     digit = temp % 10
#     sum += digit * digit * digit
#     temp = temp // 10
# if sum == num:
#     print('It is an Armstrong number')
# else:
#     print('It is not an Armstrong number')

# square root
# n=int(input("enter the no:"))
# a=(n**(0.5))
# print(a)

# conver km to miles
# n=int(input("enter the no"))
# a=n*0.62137119
# print(a)


# celusis convert faharenhesis
# n=int(input("enter the no:"))
# a=n*33.8
# print(a)


# # positive or negative
# n=int(input("enter the no"))
# if n>0:
#     print("psitive")
# elif n<0:
#     print("negative")
# else:
#      print("zero")


# pun="''[]{}!@#$%^&*Z()"
# p=input("enter string")
# for i in p:
#     if i in pun:
#         p=p.replace(i,"")
# print(p)


# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if (temp == rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")




# year=int(input("enter the year"))
# if(year % 4==0 and year % 100!=0 or year % 400==0 ):
#     print("the year is leap")
# else:
#     print("the year is not leap")

# string=(input("enter a letter:"))
# if (string==string[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")

# Find LCM and hcf

# import math as m
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# HCF = m.gcd(num1,num2)
# LCM = int((num1*num2)/(HCF))
# print("LCM of given numbers: ", LCM)
# print("HCF of given numbers: ", HCF)