# Introduction to object
class Dog(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('Nice you made a dog!')

    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old")

    def talk(self):
        print("Bark!")


class Cat(Dog):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color
        self.name = 'tech'

    def talk(self):
        print("Meow!")


jim = Dog("jim", 70)
tim = Cat('tim', 5, 'blue')
tim.speak()
