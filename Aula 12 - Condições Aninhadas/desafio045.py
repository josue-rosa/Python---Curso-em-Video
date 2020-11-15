"""programa que faça o computador jogar jokenpô com você"""

from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

jogador = int(input('''Qual é a sua jogada?
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
'''))
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 15)
print(f'O computador jogou: {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' *15)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA') 

elif computador == 1: # COMPUTADOR jogou PAPEL
    if jogador == 1:
        print('EMPATOU')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: # COMPUTADOR JOGOU TESOURA
    if jogador == 2:
        print('EMPATOU')
    elif jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
