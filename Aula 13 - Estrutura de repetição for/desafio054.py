"""programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""
from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    ano_nasc = int(input('Informe o ano de nascimento '))
    idade = date.today().year - ano_nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(maior)
print(menor)
