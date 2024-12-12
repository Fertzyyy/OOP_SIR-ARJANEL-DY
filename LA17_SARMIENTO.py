class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power = atk_power
         
    def attack(self, target):
        target.health -= self.atk_power
        target.health = max(target.health,0)
        print(f"{self.name} attacked {target.name} for {self.atk_power} damage.")
        print(f"{target.name} has {target.health} health remaining.\n")
    
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount}. Now has {self.health} health.\n")


    
player1 = Player("Clove", 100, 20)
player2 = Player("Neon", 80, 15)

while player1.health > 0 and player2.health >0:
    player1.attack(player2)
    if player2.health == 0:
        print(f"{player2.name} lose {player1.name} Wins")
        break

    player2.attack(player1)
    if player1.health == 0:
        print(f"{player1.name} lose {player2.name} Wins")
        break
    
    player1.heal(20)
    player2.heal(10)