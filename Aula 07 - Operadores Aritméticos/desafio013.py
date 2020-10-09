# ler um salario e exibir o valor com 15% de aumento
salario = float(input('Valor do salario: '))

novo_salario = salario + (salario * 15/100)  # multiplicação e divisao tem a mesma ordem de precedencia
print(f'Seu novo salario com 15% de aumento é de R$ {novo_salario:.2f}')
