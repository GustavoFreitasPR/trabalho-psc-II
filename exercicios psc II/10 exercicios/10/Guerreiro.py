import random
from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 100)

    def atacar(self, alvo):
        dano = random.randint(10, 20)
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.set_hp(alvo.get_hp() - dano)

    def habilidade_especial(self, alvo):
        print(f"{self.nome} usa Golpe Poderoso!")
        dano = random.randint(20, 30)
        print(f"{self.nome} causa {dano} de dano com Golpe Poderoso.")
        alvo.set_hp(alvo.get_hp() - dano)
