# # # def myfun(n):
# # #     return len(n)
# # # x=map(myfun,('a','b','c'))
# # # print(x)
# # # print(list(x))
# # #
# # # def demo(name, age):
# # #     # print value
# # #     print(name, age)
# # # demo("Ben", 25)
# #
# # def calculation(a, b):
# #     addition = a + b
# #     subtraction = a-b
# #     return addition
# #     return subtraction
# # # get result in tuple format
# # res = calculation(40, 30)
# # print("addition:",res)
# # print("subtraction:",res)
# #
# # def calculation(a, b):
# #     return a + b, a - b
# # # get result in tuple format
# # # unpack tuple
# # add, sub = calculation(40, 10)
# # print(add, sub)
# #
# # def show_employee(name, salary=9000):
# #     print("Name:", name, "salary:", salary)
# #
# # show_employee("Ben", 12000)
# # show_employee("Jessa")
#
# # b = "Hello, World!"
# # print(b[:5])
#
# # lambda arguments : expression
# # lambda fn using map fn
#
# # n=[4,9,5,7]
# # print(list(map(lambda x:x**2,n)))
# #
# #
# # n=[0, 1, 2, 3, 5, 8, 13]
# # print(list(filter(lambda x:x%2!=0,n)))
# #
# # import functools
# # lis = [1, 3, 5, 6, 2]
# # print(functools.reduce(lambda x, y: x+y, lis))
#
# # class animal():
# #     def animalshow(self):
# #         print("happy")
# # class dog(animal):
# #     def dogshow(self):
# #         print("dog haappu")
# # class dogboy(dog,animal):
# #     def show(self):
# #         print("happy dog boy")
# # obj=animal()
# # obj.animalshow()
#
# # class animal():
# #     def animalshow(self):
# #         print("happy animal")
# # class aniaml1():
# #     def animal1show(self):
# #         print("happy animal1")
# #
# # class aniaml2():
# #     def animal2show(self):
# #         print("happy animal2")
# #
# # class aniaml3():
# #     def animal3show(self):
# #         print("happy animal3")
# #
# # class dog(animal,aniaml1,aniaml2,aniaml3):
# #     def dogshow(self):
# #         print("happy dog")
# #
# # obj=dog()
# # obj.animalshow()
# # obj.animal1show()
# # obj.animal2show()
# # obj.animal3show()
# # obj.dogshow()
#
#
# # x = lambda a, b, c : a + b + c
# # print(x(5, 6, 2))
#
#
# # class animal():
# #     def __init__(self):
# #         print("animal")
# #     def _animalshow(self):
# #         print("ftyhv")
# # class animal1():
# #     def __payal__(self):
# #         print("gty")
#
#
#
# def sum(*args):
#     s=0
#     for i in args:
#         s+=i
#     print("sum is",s)
# sum(10,20,30,40)
#
# def three(a,b,c):
#     print(a,b,c)
# args=[1,2,3]
# three(*args)
#
# def three(a,b,c):
#     print(a,b,c)
# three(a="one",b="raj",c="priti")
#
#
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
#
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#
#
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
# myFun(first='Geeks', mid='for', last='Geeks')
#
# def myfun(**kwargs):
#     for i,j in kwargs.items():
#         print("%s : %s" %(i,j))
# myfun(name='payal',age=26,sub="math")

