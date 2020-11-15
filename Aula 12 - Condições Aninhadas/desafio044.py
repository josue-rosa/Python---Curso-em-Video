"""Programa que calcule o valor a ser pago por um produto, considerando o seu Preço normal e condição de pagamento

- a vista dinheiro/cheque: 10% de desconto
- a vista cartao: 5% de desconto
- em até 2x no cartao: preço normal
- em 3x ou mais no cartão: 20% juros
"""
valor_produto = float(input('Informe o valor do produto: '))

opcao = int(input("""Informe a forma de pagamento.
[1] - Para pagamento á vista/Cheque: com 10% de desconto.
[2] - A vista no cartão: 5% de desconto.
[3] - em 2x no cartão: Preço normal.
[4] - em 3x ou mais no cartão: 20% de juros.
"""))

if opcao == 1:
    vista_din_cheque = valor_produto - (valor_produto * 0.10)
    print(f'O valor do produto com 10% de desconto ficou: R$ {vista_din_cheque:.2f}')
elif opcao == 2:
    vista_cartao = valor_produto - (valor_produto * 0.05)
    print(f'O valor do produto com 5% de desconto ficou: R$ {vista_cartao:.2f}')
elif opcao == 3:
    parcelado_2x_cartao = valor_produto / 2
    print(f'Nesta condição, você não tem desconto. O valor de {valor_produto:.2f} parcelado em 2x ficou R$ {parcelado_2x_cartao:.2f}')
elif opcao == 4:
    print('Atenção. Nesta forma de pagamento, há 20% de juros')
    parcelado_3x_mais_cartao = valor_produto + (valor_produto * 0.20)
    total_parcelas = int(input('Quantidade de parcelas? '))
    parcela = parcelado_3x_mais_cartao / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f} COM JUROS. O valor do final do produto será R$ {parcelado_3x_mais_cartao:.2f}')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente')

