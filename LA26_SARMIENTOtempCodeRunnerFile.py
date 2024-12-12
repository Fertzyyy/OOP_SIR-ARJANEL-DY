from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name 
    
    @abstractmethod
    def attack(self):
        pass
    
class Warrior(GameCharacter):
    def attack(self):
        print("Swings Sword!")      
        
class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")   