class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.__saldo = saldo  # Usamos o duplo underscore para encapsular o saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} feito na conta de {self.titular}. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Retirada de R${valor} da conta de {self.titular}. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def __str__(self):
        return f"Conta de {self.titular}"