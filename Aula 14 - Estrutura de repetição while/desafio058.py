"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer
"""

from random import randint

tentativas = 1
computador = randint(1, 4)
jogador = int(input('Informe um numero para jogarmos '))

while jogador != computador:
    jogador = int(input('Errou. Tente novamente'))
    tentativas += 1
print(f'Acertou. Pensei no {computador} também')
print(f'Total de tentativas {tentativas}')



"""
computador = randint(1, 4)
for c in computador:
    print(c)
"""