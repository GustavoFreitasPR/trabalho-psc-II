from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

    def correr(self):
        print(f'A {self._tipo}, está correndo a {self._velocidade}km/h')
