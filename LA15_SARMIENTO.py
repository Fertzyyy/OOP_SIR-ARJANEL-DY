class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Bark!")
        
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Meow!")
        
class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Chirp!")
        
class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("...")
        
Aso = Dog ("Akita")
Pusa = Cat ("Siamese")
Ibon = Bird ("Owl")
Isda = Fish ("Mlikfish")

def animal_sounds(animal):
    animal.speak()

for animal in [Aso, Pusa, Ibon, Isda]:
    animal_sounds(animal)