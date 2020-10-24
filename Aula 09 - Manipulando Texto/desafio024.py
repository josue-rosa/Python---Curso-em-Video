"""
crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"
"""
'''
cidade = str(input('Informe o nome da cidade: ')).strip().lower()
spliter = cidade.split()
if spliter[0] == 'santo':
    print("True")
else:
    print("False")
'''

# Outra forma mais compacta de resolver.
# CORREÇÃO DO GUANABARA

cidade = str(input('Digite a cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
# [:5] é a mesma coisa que: começa na posição 0 e vai até a posição 4. Que é um total de 5 caracteres.
