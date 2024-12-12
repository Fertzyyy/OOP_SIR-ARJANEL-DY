class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)

my_phone = Android("Samsung", "Galaxy S21")

my_phone.describePhone()