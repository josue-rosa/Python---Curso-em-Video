"""
# Exemplo de condição simples

nome = str(input('Qual seu nome: '))
if nome == 'Josué':
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}')

# Exemplo de condição composta. Nesse caso é quando tem o ELSE
nome = str(input('Qual seu nome: '))
if nome == 'Josué':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal.')
print(f'Bom dia, {nome}')
"""


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média foi {media:.2f}')
'''
if media >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média foi ruim. Estude mais!')
'''
# o if também pode ser escrito de forma simplificada.
print('PARABÉNS' if media >= 6.0 else 'ESTUDE MAIS')
