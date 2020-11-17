"""programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""
from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    ano_nasc = int(input(f'Informe o ano de nascimento da {c}ª pessoa '))
    idade = date.today().year - ano_nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoa(s) são MAIORES de idade')
print(f'{menor} pessoa(s) são MENORES de idade')
