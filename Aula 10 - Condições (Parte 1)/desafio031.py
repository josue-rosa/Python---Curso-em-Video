"""
Programa que pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 po km para viagens até 200km
e R$ 0,45 para viagens mais longas
"""
distancia = float(input('Informe a distancia em km: '))
'''
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O valor da passagem é de R$ {distancia * 0.45:.2f}')

'''

# Outra forma de fazer a partir do IF
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O valor da passagem é de R${preco:.2f}')
