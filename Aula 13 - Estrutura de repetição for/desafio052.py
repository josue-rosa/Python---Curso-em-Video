"""Programa que leia um numero inteiro e diga se ele é ou não
um número primo"""
total = 0
print('''
Pra ser PRIMO, um número tem que ser divisível por 1 e por ELE MESMO. 
Portanto, ele será divisivel 2 vezes.
''')
numero = int(input('Digite um numero: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisivel {total} vezes')
if total == 2:
    print('portanto, ELE É PRIMO')
else:
    print('Portanto, NÃO É PRIMO')
