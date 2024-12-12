class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"Car brand: {self.brand}, color: {self.color}"

c1 = car("Toyota", "Black")
print(f"Original value of c1: {c1}")

c1.color = "Red"
print(f"Updated value of c1: {c1}")

c2 = car("Nissan", "White")
print(f"Original value of c2: {c2}")

print(f"Final value of c1: {c1}")
print(f"Final value of c2: {c2}")