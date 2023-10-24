from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0.0, limite_cheque_especial=1000.0):
        super().__init__(titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if 0 < valor <= (self.get_saldo() + self.limite_cheque_especial):
            self._saldo = valor
            print(f"Retirada de R${valor} da conta corrente de {self.titular}. Saldo atual: R${self.get_saldo():.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido")