class Carro():
    def __init__(self, modelo, ano):
        self._modelo = modelo
        self._ano = ano

    def acelerar(self):
        print(f'O carro {self._modelo} do ano {self._ano}, ACELEROU')


