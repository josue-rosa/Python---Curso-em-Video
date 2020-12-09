"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer
"""
"""
from random import randint

tentativas = 1
computador = randint(0, 10)
jogador = int(input('Informe um numero para jogarmos '))

while jogador != computador:
    jogador = int(input('Errou. Tente novamente. '))
    tentativas += 1
print(f'Acertou. Pensei no {computador} também.')
print(f'Total de tentativas {tentativas}.')
"""

# Corrigido do Professor
from random import randint
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais..Tente mais uma vez.')
        elif jogador > computador:
            print('Menos. Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
