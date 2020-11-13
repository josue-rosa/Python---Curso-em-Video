"""Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

calcule o valor prestação mensal sabendo que ele não pode exceder 30% do salario ou então o emprestimo será negado
"""

valor_casa = float(input('Qual o valor da casa? R$ '))
salario_comprador = float(input('Qual o salário do comprador? R$ '))
qtd_anos = int(input('Quantidade de anos para pagar? '))

calculo_prestacao = valor_casa / (qtd_anos * 12) # conversão de tempo em ANOS para MÊS

# Calculo de 30% do salario
calculo_30salario = (salario_comprador * 0.30) 

print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {qtd_anos} anos, a prestação será de R$ {calculo_prestacao:.2f}')
if calculo_prestacao > calculo_30salario:
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado')
