class super():
    def __init__(self):
        self._value1=100
        self.__value2=200
    def display(self):
        print(self._value1)
        print(self.__value2)
class sub(super):  #sub class madhe only protect value show hote value1 karan value value2 private ahe
    def show(self):
        print(self._value1)
        print(self.__value2)
s=super() #super class cha object banala t display method ni donhi show honar
s.display()
s1=sub()
s1.show()
# class abc():
#     def __init__(self):
#         self._v=100
#         self._v1=200
#     def display(self):
#         print(self._v)
#         print(self._v1)
# s=abc()
# # s.display()
# s.display()
#private
# class emp():
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def show(self):
#         print("name:",self.name,'salary:',self.__salary)
# emp1=emp('payal',2000)
# emp1.show()

# #private
# class company():
#     def __init__(self):
#         self._project="measstro"
#     def show1(self):
#         print("project:", self._project)
# class emp(company):
#     def __init__(self,name):
#         self.name=name
#
#     def show(self):
#         print("name:",self.name)
#         # print("project:",self._project)
# emp1=emp('payal')
# emp1.show()
#
# c=company()
# c.show1()


