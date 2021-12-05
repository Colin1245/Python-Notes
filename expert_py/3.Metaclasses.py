class Test:
    pass


class Foo():
    def show(self):
        print("HI")


def add_attribute(self):
    self.z = 9


Test = type('Test', (Foo,), {"x":5, "add_attribute":add_attribute})
t = Test()
t.add_attribute()
t.wy = "hello"

# print(type(Test))
# print(t.wy)
# print(t.z)
# print(type)


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)

    def __init__():
        pass

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

d = Dog()
print(d.HELLO())