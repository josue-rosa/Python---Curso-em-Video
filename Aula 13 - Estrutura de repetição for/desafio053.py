"""Programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços"""

# Exemplo: Apos a Sopa, A sacada da casa, a torre da derrota

frase = str(input('digite uma frase: ')).lower().strip()

print(f'{frase} ao contrário fica: {frase[::-1]}. \nPortanto, ', end='')

if frase == frase[::-1]:
    print('Esta frase é um palíndromo')
else:
    print('Não é palindromo')
