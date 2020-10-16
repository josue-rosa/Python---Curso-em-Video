"""
crie um programa que leia uma numero Real qualquer pelo teclado e mostre sua porção inteira
Ex: 6.127 tem a parte inteira 6
"""

from math import trunc
num = float(input("Digite um numero: "))
print(f'Este numero tem a parte inteira {trunc(num)}')
