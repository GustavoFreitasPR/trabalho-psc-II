from Imprimivel import Imprimivel

class Carro(Imprimivel):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def imprimir(self):
        print(f"Carro: {self.marca} {self.modelo} ({self.ano}), Cor: {self.cor}")
