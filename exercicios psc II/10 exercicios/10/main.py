from Personagem import Personagem
from Mago import Mago
from Guerreiro import Guerreiro
from Arqueiro import Arqueiro

import random

def simular_jogo():
    guerreiro = Guerreiro("Guerreiro")
    mago = Mago("Mago")
    arqueiro = Arqueiro("Arqueiro")

    while guerreiro.get_hp() > 0 and mago.get_hp() > 0 and arqueiro.get_hp() > 0:
        atacante = random.choice([guerreiro, mago, arqueiro])
        alvo = random.choice([p for p in [guerreiro, mago, arqueiro] if p != atacante and p.get_hp() > 0])

        atacante.atacar(alvo)

        if random.random() < 0.3:
            atacante.habilidade_especial(alvo)

        print(f"{alvo.nome} tem {alvo.get_hp()} pontos de vida restantes.")

    vencedor = [p for p in [guerreiro, mago, arqueiro] if p.get_hp() > 0][0]
    print(f"{vencedor.nome} venceu o jogo!")

    
# Iniciar o jogo
simular_jogo()