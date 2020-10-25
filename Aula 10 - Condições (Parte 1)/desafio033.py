"""
Programa que leia 3 numeros e diga qual é o maior e qual o menor.
"""

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
if n1 > n2 and n3:
    print(f' {n1} é o maior')
elif n2 > n1 and n3:
    print(f'{n2} é o maior')
else:
    print(f'{n3} é o maior')
