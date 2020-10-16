"""
import math
num = int(input("Digite um numero: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é igual a {raiz:.2f}")
print("")
print(f"Arredondando para cima: {math.ceil(raiz):.2f}")
print(f"Arredondando para baixo: {math.floor(raiz):.2f}")
"""

# Também é possível importar diretamente os múdulos sqrt, ceil e floor
"""from math import sqrt, ceil, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f}')
print(f'Arredondando para cima: {ceil(raiz):.2f}')
print(f'Arredondando para baixo: {floor(raiz):.2f}')
"""

import random
""" Exibir um valor ramdomico entre 0 e 1
num = random.random()
print(num)
"""

""" Exibir um valor ramdomico INTEIRO entre 1 e 10
num = random.randint(1, 10)
print(num)
"""

import emoji
print(emoji.emojize("Olá Mundo, :sunglasses:", use_aliases=True))
