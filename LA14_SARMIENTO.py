class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describespiderman(self):
        print(f"Spidermans name: {self.name},Spidermans age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

Spiderman1 = Tobey("Tobey Maguire", 49, "Spider-Man") 
Spiderman2 = Andrew("Andrew Garfield", 41, "The Amazing Spider-Man") 
Spiderman3 = Tom("Tom Holland", 28, "Spider-Man No Way Home") 

print(Spiderman1.name.upper(), Spiderman1.movieTitle)
print(Spiderman2.name.upper(), Spiderman2.movieTitle)
print(Spiderman3.name.upper(), Spiderman3.movieTitle)