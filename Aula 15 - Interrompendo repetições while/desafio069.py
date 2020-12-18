tot18 = totalH = totalM_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    if idade > 18:
        tot18 += 1

    if sexo == 'M':
        totalH += 1

    if sexo == 'F' and idade < 20:
        totalM_20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totalH} homens cadastrados.')
print(f'E temos {totalM_20} mulheres com menos de 20 anos.')


# Meu código

"""
resp = 'S'
idade = int(input('Informe a idade: '))
sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
maior18 = sexo_masc = total_mulher_menor_20 = 0

while resp == 'S':
    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        sexo_masc += 1
    elif sexo in 'Ff' and idade < 20:
        total_mulher_menor_20 += 1

    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Ss':
        idade = int(input('Informe a idade: '))
        sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]

print(f'Foram encontradas {maior18} Pessoas acima de 18 anos.')
print(f'{sexo_masc} homens foram cadastrados')
print(f'{total_mulher_menor_20} mulheres tem menos de 20 anos.')
"""
