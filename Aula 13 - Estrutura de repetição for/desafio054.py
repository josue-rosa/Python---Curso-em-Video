"""programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""
from datetime import date

maior = 0
menor = 0
for c in range(1, 5):
    ano_nasc = int(input('Informe o ano de nascimento '))
    maioridade = date.today().year - ano_nasc
    if maioridade >= 21:
        maior = c
    else:
        menor = c
print(maior)
print(menor)

