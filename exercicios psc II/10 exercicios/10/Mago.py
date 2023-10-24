import random
from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 80)

    def atacar(self, alvo):
        dano = random.randint(15, 25)
        print(f"{self.nome} lança uma bola de fogo em {alvo.nome}, causando {dano} de dano.")
        alvo.set_hp(alvo.get_hp() - dano)

    def habilidade_especial(self, alvo):
        print(f"{self.nome} conjura um Raio de Gelo!")
        dano = random.randint(25, 35)
        print(f"{self.nome} causa {dano} de dano com o Raio de Gelo.")
        alvo.set_hp(alvo.get_hp() - dano)
