"""Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

calcule o valor prestação mensal sabendo que ele não pode exceder 30% do salario ou então o emprestimo será negado
"""

valor_casa = float(input('Qual o valor da casa, em R$: '))
salario_comprador = float(input('Qual o salário do comprador? '))
qtd_anos = int(input('Quantidade de anos para pagar? '))

calculo = valor_casa / qtd_anos

print(calculo)
