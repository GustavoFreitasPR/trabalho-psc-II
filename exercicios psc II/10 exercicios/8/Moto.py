from Imprimivel import Imprimivel

class Moto(Imprimivel):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def imprimir(self):
        print(f"Moto: {self.marca} {self.modelo} ({self.ano}), Cor: {self.cor}")