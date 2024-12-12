class Appliances:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model   
    def operate(self):
        print("Operating")
    def info(self):
        print(f"Brand:{self.brand}, Model:{self.model}")
        
class WashingMachine(Appliances):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operation(self):
        print("Washing Machine: Washing clothes!")
        
class Refrigirator(Appliances):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operation(self):
        print("Refrigirator: Keeping food cold!")
        
class Microwave(Appliances):
    def __init__(self, brand, model):
        Appliances.__init__(self, brand, model)
    def operation(self):
        print("Microwave: Heating food!")
    
Ap1 = WashingMachine ("Haier", "HWD120-B14979S8")
Ap2 = Refrigirator ("Samsung","RT20FARVDSA")
Ap3 = Microwave ("Fujidenzo", "MM-22 BL")
    
for appliances in [Ap1,Ap2,Ap3]:
    appliances.operation()
    appliances.info()