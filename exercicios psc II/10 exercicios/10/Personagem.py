class Personagem:
    def __init__(self, nome, hp):
        self.nome = nome
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp

    def atacar(self, alvo):
        pass

    def habilidade_especial(self, alvo):
        pass