
nome_produto = str(input('Nome do produto: ')).strip()
preco_produto = float(input('Preço: '))
resp = 'S'
valor_total_produtos = 0
cont_preco = 0

while True:
    if preco_produto > 1000.0:
        cont_preco += 1

    valor_total_produtos += preco_produto

    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Ss':
        nome_produto = str(input('Nome do produto: ')).strip()
        preco_produto = float(input('Preço: R$ '))
    else:
        break

print(f'Gasto total em compras: R${valor_total_produtos:.2f}')
print(f'{cont_preco} produtos custam acima de MIL Reais')
