class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car brand: {self.brand}"

my_car = Car("Toyota")

print(my_car)

del my_car

print(my_car)