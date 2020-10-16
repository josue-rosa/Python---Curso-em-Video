"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- o nome com todas as minusculas
- Quantas letras ao todo sem considerar os espaços.
- Quantas letras tem o primeiro nome
"""

nome = str(input('Informe seu nome: ')).strip()

# Transformando para maiscula
print(f'Seu nome em MAIUSCULA é {nome.upper()}')

# Transformando para minuscula
print(f'Seu nome em minusculas é {nome.lower()}')

# Quantas letras ao todo sem considerar os espaços.
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras sem considerar os espaços')


# Exercicio primeiro nome
spliter = nome.split()
print(f'Seu primeiro nome é {spliter[0]} e tem {len(spliter[0])} letras')

# Outra forma de fazer:
print(f'Outra forma. Seu primeiro nome tem {nome.find(" ")} letras.')


"""
########
Extra 1 
########
Quando pedir uma informação no input, por exemplo:
nome = input('Digite algo')

O ideal é EXPLICITAR que é uma string com str antes do input
Assim: nome = str(input('Digite algo'))

########
Extra 2
########
Também posso colocar métodos direto no input.
Ex: nome = str(input('Digite algo')).strip() # strip remove espaços no input
"""