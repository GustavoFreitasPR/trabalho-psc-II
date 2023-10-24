import random
from Personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 90)

    def atacar(self, alvo):
        dano = random.randint(12, 22)
        print(f"{self.nome} atira uma flecha em {alvo.nome}, causando {dano} de dano.")
        alvo.set_hp(alvo.get_hp() - dano)

    def habilidade_especial(self, alvo):
        print(f"{self.nome} usa Tiro Certeiro!")
        dano = random.randint(22, 32)
        print(f"{self.nome} causa {dano} de dano com Tiro Certeiro.")
        alvo.set_hp(alvo.get_hp() - dano)
