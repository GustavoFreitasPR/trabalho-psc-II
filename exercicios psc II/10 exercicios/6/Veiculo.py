class Veiculo():
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade

    def acelerar(self):
        print(f'O veiculo {self._tipo }, acelerou e agora está a {self._velocidade + 15} km/h')

    def descricao(self):
        print(f'O veiculo {self._tipo }, é da cor azul e sua velocidade máxima é de {self._velocidade} km/h')