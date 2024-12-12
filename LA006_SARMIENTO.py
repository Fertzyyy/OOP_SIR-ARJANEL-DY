class laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def laptop_info(self):
        pass  

my_laptop = laptop("Lenovo", "Ideapad Gaming 3")

print(my_laptop.laptop_info())