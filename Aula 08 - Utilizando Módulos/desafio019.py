""" um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Fazer programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""

from random import choice
alunos = ['Josué', 'Davi', 'Andreia', 'Paloma']
sorteado = choice(alunos)
print(sorteado)


# Resposta do Guanabara
"""from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('Terceiro aluno'))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
"""




"""
Referencia sobre Choice
https://docs.python.org/pt-br/3.8/library/random.html#random.choice
"""