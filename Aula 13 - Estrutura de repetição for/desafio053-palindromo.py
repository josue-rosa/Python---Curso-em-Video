"""Programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços"""

# Exemplo: Apos a Sopa, A sacada da casa, a torre da derrota

frase = str(input('digite uma frase: ')).lower().strip()
spliter = frase.split()
junto = ''.join(spliter)
frase_inverso = junto[::-1]

print(f'O inverso de {junto} é {frase_inverso}')

if frase_inverso == junto:
    print('Esta frase é um palíndromo')
else:
    print('Não é palindromo')
