"""
programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1250, calcule um aumento de 10%
Para inferiores, 15% de aumento
"""
'''
salario = float(input('Valor do seu salário em R$ '))
if salario >= 1250:
    print(f'Seu novo salário com aumento de 10% fica, R$ {salario + (salario * 0.10)}')
else:
    print(f'Seu novo salário com aumento de 15%, fica R$ {salario + (salario * 0.15):.2f}')


'''
salario = float(input('Valor do seu salário em R$ '))
if salario >= 1250:
    Novo_salario = salario + (salario * 0.10)
else:
    Novo_salario = salario + (salario * 0.15)
print(f'Quem ganhava R${salario:.2f}, passa a receber agora R${Novo_salario:.2f}')
