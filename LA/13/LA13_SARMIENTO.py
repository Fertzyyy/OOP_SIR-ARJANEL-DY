class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

class Fish(Animal):
    def __init__(self, name, animal_type, can_swim):
        super().__init__(name, animal_type)
        self.can_swim = can_swim

fish = Fish("Goldfish", "Aquatic", True)

print(f"Can the {fish.name} swim? {fish.can_swim}")
