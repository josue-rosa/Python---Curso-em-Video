"""Programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e menor peso lidos"""

maior_peso = 0
menor_peso = 0
for c in range(1, 4):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi {maior_peso}Kg')
print(f'O menor peso lido foi {menor_peso}Kg')
