"""
Faça um programa que leia o sexo de uma pessoa. Mas só aceite os valores
'M' ou 'F'. caso esteja errado, peça a digitação novamente até ter um valor correto
"""

sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Valor inválido. Digite novamente [M/F] ')).upper().strip()[0]
print(f'sexo {sexo} registrado com sucesso')
