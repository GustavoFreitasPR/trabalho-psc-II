class Carro():
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano

    def acelerar(self):
        print(f'O carro {self.__modelo} do ano {self.__ano} acelerando!!')
