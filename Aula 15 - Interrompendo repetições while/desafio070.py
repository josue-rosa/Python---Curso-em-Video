
resp = 'S'
idade = int(input('Informe a idade: '))
sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
maior18 = 0

while resp == 'S':
    if idade > 18:
        maior18 += 1
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Ss':
        idade = int(input('Informe a idade: '))
        sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]


print(f'{maior18} Pessoas acima de 18 anos')
