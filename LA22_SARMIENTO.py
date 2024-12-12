class BirthdayParty:
    def __init__(self, theme, foods, special_dish):
        self.theme = theme
        self.foods = foods
        self.special_dish = special_dish
    
    def __secret_dish(self):
        print("Secret Dish: Lumpiang Shanghai")
    
    def show_foods(self):
        print(f"Theme: {self.theme}")
        print("Food list:")
        for food in self.foods:
            print(f"- {food}")
        print(f"Special Dish: {self.special_dish}")
        self.__secret_dish() 

party1 = BirthdayParty("Beach Party", ["Grilled Fish", "Tacos", "Fruit Salad"], "Seafood Paella")
party2 = BirthdayParty("Retro Party", ["Hotdogs", "Egg Sandwich", "Jello"], "Cheese Fondue")
party3 = BirthdayParty("Baranggay Party", ["Pineapple Skewers", "BBQ Chicken", "Rice"], "Lechon")

party1.show_foods()
print("\n")
party2.show_foods()
print("\n")
party3.show_foods()
