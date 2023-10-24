from Forma import Forma

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        super().__init__()
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura