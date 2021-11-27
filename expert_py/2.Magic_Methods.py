class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
        return rep



p = Person("tim", 18)
print(repr(p))