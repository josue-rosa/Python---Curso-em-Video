# ler um salario e exibir o valor com 15% de aumento
salario = float(input('Valor do salario: '))

novo_salario = salario + (salario * 0.15)
print(f'Seu novo salario com 15% de aumento é de R$ {novo_salario:.2f}')
