# def add(num1, num2):     return num1 + num2
# def sub(num1, num2):     return num1 - num2
# def multi(num1, num2):     return num1 * num2
# def div(num1, num2):     return num1 / num2
# def module(num1, num2):     return num1 % num2
# def Exponentiation(num1, num2):     return num1 ** num2
# def Floordivision(num1, num2):     return num1 // num2
# print("Select operation: \n"
#       "1. add:\n"
#       "2. sub:\n"
#       "3. multi:\n"
#       "4. div:\n"
#       "5. module:\n"
#       "6. Exponentiation:\n"
#       "7. Floor division:\n")
# select = int(input("select one operations 1, 2, 3, 4, 5, 6, 7:\n"))
# num1 = int(input("enter first no:\n"))
# num2 = int(input("enter second no:\n"))
# if select == 1:
#     print(num1, "+", num2, "=", add(num1, num2))
# elif select == 2:
#     print(num1, "-", num2, "=", sub(num1, num2))
# elif select == 3:
#     print(num1, "*", num2, "=", multi(num1, num2))
# elif select == 4:
#     print(num1, "/", num2, "=", div(num1, num2))
# elif select == 5:
#     print(num1, "%", num2, "=", module(num1, num2))
# elif select == 6:
#     print(num1, "**", num2, "=", Exponentiation(num1, num2))
# elif select == 7:
#     print(num1, "//", num2, "=", Floordivision(num1, num2))
# else:
#     print("invalid input")
#

x=int(input("enter first no.:"))
y=int(input("enter second no.:"))
op=input("enter to choose: 1.) addition 2.) sub 3.) mult 4.) div")
if op =="1":
    print(x+y)
elif op =="2":
    print(x-y)
elif op == "3":
    print(x*y)
elif op =="4":
    print(x/y)
else:
    print("wrong input") 