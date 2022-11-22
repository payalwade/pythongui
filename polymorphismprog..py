# #method overriding means same function name and call fist object create
# class Abc():
#     def van(self):#filstly create object then print
#         print("welcome van")
# class BCD(Abc):
#     def van(self):#call
#         print("welcome van2")
#     def show(self):
#         print("show data")
#
# a=BCD()
# a.van()
# a.show()



# class abc():
#     def show(self,a,b):
#         c=a+b
#         print("show1")
#         print(c)
#     def display(self):
#         print("display1")
# class bcd(abc):
#     def show(self,a,b):
#         c=a-b
#         print("show2")
#         print(c)
#     def display(self):
#         print("display2")
# obj1=abc()
# obj1.show(1,2)
# obj1.display()
#
# obj=bcd()
# obj.show(2,1)
# obj.display()
#
