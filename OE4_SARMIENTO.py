class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
         
    def attack(self, target):
        target.health = target.health - self.power
        print(f" The attacker {self.name} attacked {target.name} and the remaining health is {target.health}\n")
    
    def heal(self, special_move):
        self.health += special_move
        print(f"{self.name} healed for {special_move}. Now has {self.health} health.\n")
        
    def special_move(self):
        pass

class Warrior(Character):
    def special_move(self):
        print("Warrior uses Sheild Bash!")
        self.power = self.power + self.power

class Mage(Character):
    def special_move(self):
        print("Mage cast Fireball!")
        target.health = target.health - 100

        
class Archer(Character):
    def special_move(self):
        print("Archer shoots a Piercing Arrow")
        target.health = target.health - 200

class Monster(Character):
    def special_move(self):
        print("Monster roars and gain extra health!")
        self.health + 50
        print(f"{self.name} health is now {self.health}")

Warrior1 = Warrior ("Zilong", 2000 , 120 )
Mage1 = Mage ("Nana", 1500 , 100 )
Archer1 = Archer ("Miya", 1000, 150 )

Monster1 = Monster ("Yu-Zhong", 3000, 200)

Monster1.attack(Warrior1)
Monster1.special_move
Warrior1.attack(Monster1)
Warrior1.special_move

Monster1.attack(Mage1)
Monster1.special_move
Mage1.attack(Monster1)
Mage1.special_move

Monster1.attack(Archer1)
Monster1.special_move
Archer1.attack(Monster1)
Archer1.special_move