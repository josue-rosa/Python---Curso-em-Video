"""programa que leia o ano de nascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""
from datetime import date

maior_idade = menor_idade = 0

for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c} pessoa nasceu? '))
    idade = date.today().year - nascimento

    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'{maior_idade} pessoas são maior de idade')
print(f'{menor_idade} pessoas são menor de idade')
