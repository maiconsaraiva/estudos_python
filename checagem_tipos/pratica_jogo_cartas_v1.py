"""
Praticando mais o Type Hint

Jogo de Cartas V1
"""
import random

# Constantes pra facilitar a manipulação
NAIPES = '♠ ♥ ♦ ♣'.split()  # ['♠', '♥', '♦', '♣']
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()  # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas"""
    baralho = [(n, c) for n in NAIPES for c in CARTAS]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return (
        baralho[0::4],  # Inicia na posição 0, e vai até o final, pulando de 4 em 4
        baralho[1::4],  # Inicia na posição 1, e vai até o final, pulando de 4 em 4
        baralho[2::4],  # Inicia na posição 2, e vai até o final, pulando de 4 em 4
        baralho[3::4]  # Inicia na posição 3, e vai até o final, pulando de 4 em 4
    )


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    baralho = criar_baralho(True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {jogador: mao for jogador, mao in zip(jogadores, distribuir_cartas(baralho))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j,c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
