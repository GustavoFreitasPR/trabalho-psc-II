from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca


conta_poupanca = ContaPoupanca("Gabriel", 7000.0)
conta_corrente = ContaCorrente("Arthur", 5000.0)

conta_poupanca.depositar(500)
conta_poupanca.sacar(200)
conta_corrente.sacar(8000)

conta_corrente.depositar(200)
conta_corrente.sacar(800)
conta_corrente.sacar(8000)

print(conta_poupanca)
print(conta_corrente)
