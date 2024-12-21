class character():
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return "This is character object"
    

    def describe(self, course):
        print(f"Si {self.name} ay {self.age} taong gulang na sa {course}.")
        
    def section(self):
        return(f"Si {self.name} ay nasa section ng 2A")
               
student = character("Deangelo", 19)
print(student.section())