# class Test:
#     pass

class Foo():
    def show(self):
        print("HI")


def add_attribute(self):
    self.z = 9


Test = type('Test', (Foo,), {"x":5, "add_attribute":add_attribute})
t = Test()
t.add_attribute()
t.wy = "hello"

print(type(Test))
print(t.wy)
print(t.z)
# print(type)


