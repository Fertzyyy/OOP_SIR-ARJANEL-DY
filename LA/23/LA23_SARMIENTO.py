class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    
    def introduce(self, func):
        def pln(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return pln

MyHeroAcademia = AnimeCharacter("Deku", "All for One")

@MyHeroAcademia.introduce
def character_info():
    print(f"I am {MyHeroAcademia.name} and I can use {MyHeroAcademia.ability}")

character_info()
