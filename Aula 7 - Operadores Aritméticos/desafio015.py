'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

km_percorridos = float(input('Informe a quantidade de km percorridos: '))
qtd_dias = int(input('Informe quantos dias o carro ficou alugado: '))

valor_diaria = 60 * qtd_dias
valor_km_rodado = 0.15 * km_percorridos

print(f'O valor da diária ficou em R$ {valor_diaria:.2f} e o valor do Km ficou R$ {valor_km_rodado:.2f}\nSomando R$ {valor_diaria+valor_km_rodado:.2f}')

