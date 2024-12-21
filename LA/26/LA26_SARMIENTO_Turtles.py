from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    pass
    @property
    @abstractmethod    
    def alias(self):
        pass
    
class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
    
    @property 
    def alias (self):
        return self.__alias

class Michaelangelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property 
    def alias (self):
        return self.__alias

class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property 
    def alias (self):
        return self.__alias

class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias
        
    @property 
    def alias (self):
        return self.__alias
    
if __name__ == "__main__":
    print("Hell World")