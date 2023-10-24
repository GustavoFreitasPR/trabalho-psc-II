from Forma import Forma

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2