class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Noli Me Tángere", "Jose Rizal")
print(b1.title) 

b2 = Book("El Filibusterismo", "Jose Rizal")

del b1.author

print(b1.author) 

print(b2.author) 