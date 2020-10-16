""" um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Fazer programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""
import random

alunos = ['Josué', 'Davi', 'Andreia', 'Paloma']
sorteado = random.choice(alunos)
print(sorteado)


"""
Referencia sobre Choice
https://docs.python.org/pt-br/3.8/library/random.html#random.choice
"""