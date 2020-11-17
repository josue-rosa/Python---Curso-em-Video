"""Programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e menor peso lidos"""


maior_peso = 0
menor_peso = 0
for c in range(1, 4):
    peso = float(input('Informe seu peso: {kg} '))
    if peso == peso:
