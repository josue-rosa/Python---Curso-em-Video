"""Programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e menor peso lidos"""


maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe seu peso: {kg} '))
    if peso > peso:
        maior = peso
    else:
        menor = peso
print(maior)
print(menor)
