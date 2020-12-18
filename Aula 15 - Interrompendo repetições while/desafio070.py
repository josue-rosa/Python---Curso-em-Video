total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        barato = produto
        menor = preco

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(" Fim do programa "))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1.000 ')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


# Meu código
# Faltou fazer o nome do produto mais barato

"""
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
"""
