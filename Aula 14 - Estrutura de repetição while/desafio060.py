"""
leia um numero qualquer e mostre o seu Fatorial
Ex: 5! = 5x4x3x2x1 = 120
"""

num = int(input('Informe o numero para ver seu fatorial: '))
c = num
f = 1
print(f'Calculando o fatorial de {num}!')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')


# Outra forma de fazer
"""
from math import  factorial
n = int(input('Digite o numero: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')
"""