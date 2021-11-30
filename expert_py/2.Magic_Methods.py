from queue import Queue as q
import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
        return rep

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")

        self.name = self.name * x

    def __call__(self):
        print("called this function", y)

    def __len__(self):
        return len(self.name)




# p = Person("tim", 18)
# # print(repr(p))
# p * 4
# print(len(p))

class Queue(q):
    def __repr__(self):
        # return f"Queue({self._qsize()}"
        return f"{self._qsize()}"

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()


# print(q)
# print(inspect.getsource(Queue))

qu = Queue()
qu + 9
qu + 7
qu - None
print(qu)