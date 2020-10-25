""" escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
O programa devera escrever na tela se o usuário venceu ou perdeu."""

import random
print('Pensei em um numero entre 1 e 5')
computer = random.randint(0, 5)
num = int(input('Digite o seu numero: '))
if num == computer:
    print('Acertou. Parabens! ')
else:
    print(f'Errou. Pensei no {computer}. Tente outra vez')
