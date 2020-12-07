""" escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
O programa devera escrever na tela se o usuário venceu ou perdeu."""

import random
from time import sleep

print('Pensei em um numero entre 0 e 5')
computer = random.randint(0, 5)
jogador = int(input('Digite o seu numero: '))
print('Processando...')
sleep(0.5)
if jogador == computer:
    print('Acertou. Parabens! ')
else:
    print(f'Errou. Pensei no número {computer}. Tente outra vez')
