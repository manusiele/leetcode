from threading import Semaphore

class Foo:
    def __init__(self):
        self.sem2 = Semaphore(0)
        self.sem3 = Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.sem2.release()

    def second(self, printSecond):
        self.sem2.acquire()
        printSecond()
        self.sem3.release()

    def third(self, printThird):
        self.sem3.acquire()
        printThird()