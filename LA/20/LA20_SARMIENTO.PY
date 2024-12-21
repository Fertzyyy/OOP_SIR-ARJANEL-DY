class TofuBaboy:
    def __init__(self, meat, onion, black_beans, chilli, tofu, vinegar):
        self.meat = meat
        self.onion = onion
        self.black_beans = black_beans
        self.__chilli = chilli
        self.tofu = tofu
        self.vinegar = vinegar
        
    def __str__(self):
        return f"My favorite dish is Tokwat Baboy and its ingredients are {self.meat}, {self.onion}, {self.black_beans}, {self.__chilli}, {self.tofu}, {self.vinegar}"
    
    def my_chilli(self):
        return self.__chilli
            
    """def my_chilli(self, bata):
        if not bata:
            return self.__chilli
        else:
            return "secret"""
    
Tokwat_Baboy1 = TofuBaboy("Pork Liempo", "1 Red Onion", "1 can Black Beans", "3 Green Chilli", "5 Tofu cube", "200 ml Vinegar")


print(Tokwat_Baboy1.my_chilli())