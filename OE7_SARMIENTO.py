class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    
    def introduce(self, func):
        def pln(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return pln

Tekken = TekkenCharacter("Yoshimitsu", "Advanced Manji Ninjutsu")

@Tekken.introduce
def character_intro():
    print(f"I am {Tekken.name} and I can use {Tekken.ability}")

character_intro()
