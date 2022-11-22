from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        print("hello abstract")
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")
class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")
class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")
c=Car()
c.mileage()
t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()




# from abc import ABC, abstractmethod
# class Atm(ABC):
#     #abstract method
#     def machin(self):
#        print("hii")
# class Atmmachinexe(Atm):
#     def cash(self):
#         print("withdraw paise")
#     def recipt(self):
#         print("recipt mili")
#     def check(self):
#         print("balance check")
# a1=Atmmachinexe()
# a1.check()
# a1.cash()
# a1.recipt()

