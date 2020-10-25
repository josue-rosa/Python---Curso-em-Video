"""
Faça um programa que leia um numero inteiro e diga se ele é PAR
ou IMPAR
"""
numero = int(input('Informe um numero inteiro: '))
resto_Divisao = numero % 2
if resto_Divisao == 0:
    print('PAR')
else:
    print('IMPAR')
