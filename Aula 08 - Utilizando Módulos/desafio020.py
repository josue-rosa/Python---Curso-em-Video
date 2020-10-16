"""
o mesmo professor do desafio019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça programa que leia o nome dos quatro alunos e mostre a ordem sorteada
"""
import random
alunos = ['Josué', 'Davi', 'Andreia', 'Paloma']
ordemApresentacao = random.sample(alunos, len(alunos))
print(ordemApresentacao)

"""
Referencia Sample
https://docs.python.org/pt-br/3.8/library/random.html#random.sample
"""