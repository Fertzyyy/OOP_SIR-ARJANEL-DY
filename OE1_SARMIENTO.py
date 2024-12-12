class Hero:
    def __init__(self, name, role, dmg_type, health, atck_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.atck_dmg = atck_dmg

    def __str__(self):
        return f"{self.name} ({self.role}, {self.dmg_type})"

    def describe(self):
        return f"{self.name} is a {self.role} with {self.dmg_type} power. Health: {self.health}, Attack Damage: {self.atck_dmg}"

hero_mm1 = Hero("Brody", "Marksman", "Attack Damage", 2290, 105)
hero_fighter1 = Hero("Arlott", "Fighter", "Attack Damage", 2628, 120)
hero_mage1 = Hero("Lou Yi", "Mage", "Magic Damage", 2601, 107)
hero_jungle1 = Hero("Roger", "Jungler", "Attack Damage", 2530, 128)
hero_roam1 = Hero("Khufra", "Tank", "Attack Damage", 2779, 117)

def describe_team(*heroes):
    for hero in heroes:
        print(hero.describe())

describe_team(hero_mm1, hero_fighter1, hero_mage1, hero_jungle1, hero_roam1)
