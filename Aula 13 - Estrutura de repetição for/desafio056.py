"""
Programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

- A média de idade do grupo
- qual o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
"""
soma_idade = 0
# media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher = 0

for c in range(1, 5):
    print(f'------ {c}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma_idade += idade

    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    elif sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    elif sexo in 'Ff' and idade < 20:
        total_mulher += 1

# media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {soma_idade / 4}')
print(f'O nome do homem mais velho é {nome_mais_velho}')
print(f'{total_mulher} mulheres tem menos de 20 anos')
