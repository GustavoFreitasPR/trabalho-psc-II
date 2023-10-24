from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def calcular_area(self):
        pass