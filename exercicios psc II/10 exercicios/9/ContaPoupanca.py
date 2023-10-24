from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0.0):
        super().__init__(titular, saldo)
        
