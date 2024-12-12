class TofuBaboy:
    def __init__(self, meat, onion, black_beans, chilli, tofu, vinegar):
        self.meat = meat
        self.onion = onion
        self.black_beans = black_beans
        self.chilli = chilli
        self.tofu = tofu
        self.vinegar = vinegar
        
    def __str__(self):
        return f"My favorite dish is Tokwat Baboy and its ingredients are {self.meat}, {self.onion}, {self.black_beans}, {self.chilli}, {self.tofu}, {self.vinegar}"
    
Tokwat_Baboy1 = TofuBaboy("Pork Liempo", "1 Red Onion", "1 can Black Beans", "3 Green Chilli", "5 Tofu cube", "200 ml Vinegar")
Tokwat_Baboy2 = TofuBaboy("Pork Mascara", "3 White Onion", "2 can Kidney Beans", "3 red Chilli", "7 Tofu cube", "400 ml Vinegar")
Tokwat_Baboy3 = TofuBaboy("Pork", "2 Red Onion", "3 can Black Beans", "3 Green Chilli and 2 Red Chilli", "9 Tofu cube", "500 ml Vinegar")

print(Tokwat_Baboy1)
print(Tokwat_Baboy2)
print(Tokwat_Baboy3)