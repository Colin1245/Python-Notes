# Static Methods and class methods
class Dog:
    dogs = []
    xc = 5

    def __init__(self, name) -> None:
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")


class Math:
    @staticmethod
    def add(x1, x2):
        return x1 + x2


Dog.bark(5)
