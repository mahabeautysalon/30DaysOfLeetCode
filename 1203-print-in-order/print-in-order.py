from threading import Event

class Foo:
    def __init__(self):
        self.firstEvent = Event()
        self.secondEvent = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstEvent.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.firstEvent.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondEvent.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.secondEvent.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()