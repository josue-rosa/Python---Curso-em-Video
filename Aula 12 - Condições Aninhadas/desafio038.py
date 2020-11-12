"""
Programa que leia dois numero inteiros e compareos, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais
"""

num1 = int(input('Primeiro valor '))
num2 = int(input('Segundo valor '))

if num1 == num2:
    print(f'Não existe valor maior, os dois são iguais')
elif num1 > num2:
    print(f'{num1} é o maior')
else:
    print(f'{num2} é o maior')
