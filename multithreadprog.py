# Multithreading in Python without making a class

# import time
# from threading import *
# print(current_thread().getName())
# def first_thread():
#     print("my first thread running")
#     time.sleep(1)
#     print("my first thread done")
# def second_thread():
#     print("my second thread running")
#     time.sleep(1)
#     print("my second thread  done")
# Thread(target=first_thread()).start()
# Thread(target=second_thread()).start()
#

# Create Thread by extending Thread Class:

# from threading import *
# class Mythread(Thread):
#     def run(self):
#       for i in range(2):
#         print('Hi Child Thread')
# t = Mythread()
# t.start()
# for i in range(1):
#     print('Main Thread')


# from threading import *
# def mt():
#     print("Child Thread")
# child=Thread(target=mt)
# child.start()
# print("this parent thread")


# from threading import *
# class Mythread(Thread):
#     def run(self):
#         for i in range(5):
#             print("\n this is child class")
#
#
# obj=Mythread()
# t=Thread(target=obj.run())
# t.start()
# for i in range(5):
#     print("\n this is the main thread")


from threading import *
import time
class Demo:
    def num(self):
        for i in range(1,6):
            print("\n this number is",i)
            time.sleep(1)
    def double(self):
        for i in range(1,6):
            print("\n this double of number is",2*i)
            time.sleep(1)
    def square(self):
        for i in range(1,6):
            print("\n this square of number is",i*i)
            time.sleep(1)


obj=Demo()
t1=Thread(target=obj.num())
t2=Thread(target=obj.double())
t3=Thread(target=obj.square())


t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

for i in range(5):
    print("\n this is the main thread")