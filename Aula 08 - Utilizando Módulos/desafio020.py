"""
o mesmo professor do desafio019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça programa que leia o nome dos quatro alunos e mostre a ordem sorteada
"""
from random import sample
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1, n2, n3, n4]
ordemApresentacao = sample(lista, len(lista))
print(ordemApresentacao)


# Resposta do Guanabara
"""from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('Terceiro aluno'))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação sera: ')
print(lista)
"""




"""
Referencia Sample
https://docs.python.org/pt-br/3.8/library/random.html#random.sample
"""