# Animal Class
class Animal:

    def __init__(self, name, species, age):
        self.name = name
        self.specieis = species
        self.age = age

    def print_information(self, name, species, age):
        print(f"Name: {self.name} Species: {self.specieis} Age: {self.age}")

Doug = Animal("Dog", "Canine", 5)
Star = Animal("Cat", "Feline", 3)

Doug.print_information("Dog", "Canine", 5)
Star.print_information("Cat", "Feline", 3)