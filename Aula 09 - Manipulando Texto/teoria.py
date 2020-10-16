frase = 'Curso em video Python'

# técnica de fatiamento de string
print(frase[9]) # pega apenas o caractere 9
print(frase[9:13]) # começa no 9 e vai até o 13 SEM pegar ele. Muito comum em range
print(frase[9:21:2]) # do 9 ao 21 pulando de 2 em 2
print(frase[:5]) # do inicio até 5 sem, pegar o 5
print(frase[15:]) # inicia em 15 até o final
print(frase[9::3]) # inicia no 9 e vai até o final, pulando de 3 em 3.

"""
ANÁLISE
"""
print(len(frase)) # len mostra o comprimento/quatidade de caracteres na string
print(frase.count('o')) # conta quantas vezes aparece a letra "o" minuscula
print(frase.count('o', 0, 13)) # conta quantas vezes aparece a letra 'o' no intervalo de 0 ao 13 SEM contar o 13
print(frase.find('deo'))# a partir da posição 11
print(frase.find('Android')) # Retornará -1. Que significa que não foi encontrado

# usando OPERADOR "in"
print('Curso' in frase) # Existe "Curso" na frase?

"""
TRANSFORMAÇÃO
"""
print(frase.replace('Python', 'Android')) # Trocar a palavra "Python" por "Android"
print(frase.upper()) # Transforma tudo para MAIUSCULA
print(frase.lower()) # Transforma tudo para minuscula
print(frase.capitalize()) # Transforma tudo para minuscula e transforma APENAS A PRIMEIRA letra para MAIUSCULA
print(frase.title()) # Transforma as primeiras letras para MAIUSCULAS.
# Removendo espaços inuteis na cadeia de caracteres.
frase2 = '   Aprenda Python  '
print(frase2.strip()) # Remove espaços da esquerda e da direita. Ou seja, do inicio e fim da cadeia de caracteres.
print(frase2.rstrip()) # Remove apenas os espaços da direita
print(frase2.lstrip()) # Remove apenas os espaços da esquerda

"""
DIVISÃO
"""
frase3 = 'Curso em video Python'
#Split
print(frase3.split())

"""
JUNÇÃO
"""
print('-'.join(frase3))
