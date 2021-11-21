# Static and Class Methods
class person(object):
    population = 50
    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')


newPerson = person('tim', 18)

print(person.getPopulation())

print(newPerson.getPopulation())

print(person.isAdult(21))

print(newPerson.isAdult(21))