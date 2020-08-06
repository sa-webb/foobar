class Person(object):
    species = "homosapien"

    def __init__(self, name="Unknown", age=18):
        self.name = name
        self.age = age

    def talk(self):
        return "hello person"


person1 = Person()
print(person1.talk())
print(person1.species)
print(person1.name)
