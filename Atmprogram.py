# class Atm():
#     bal=1000
#     def login(self,pin):
#         if pin == 1234 :
#             print("login")
#             return True
#         else:
#             print("wrong password")
#             return False
#
#     def balance(self,amout):
#         self.bal=self.bal+amout
#
#     def withdrowI(self,amount):
#         self.bal=self.bal-amount
#
#     def display(self):
#         print("current balance is:",self.bal)
#
# obj=Atm()
# for i in range(14):
#     if obj.login(int(input("enter your pin:"))):
#         Flag=True
#         break
# if Flag:
#     while True:
#         o=input("""press b for balance press w for withdraw press e for exist""")
#         if o == 'b' or o == "C":
#             print("Total balance is ")
#             obj.display()
#         elif o=='w' or o=='W':
#             amount = int(input("enter amount for withdraw"))
#
#             if amount < obj.bal:
#                 obj.withdrowI(amount)
#             obj.display()
#         elif o == 'e' or o == 'E':
#             exit(0)
# else:
#         print("Your pin code attempt has been completed")

# for row in range(5):
#     for col in range(5):
#         if row==0 or row==4:
#            print("*",end=" ")
#         else:
#            print(" ",end=" ")
#     print()