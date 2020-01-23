from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(i)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(i)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()

print("The end!")