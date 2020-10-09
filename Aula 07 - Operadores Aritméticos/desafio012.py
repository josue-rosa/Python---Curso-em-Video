# ler valor do produto da loja e mostre o novo preço com 5% de desconto.
valor_produto = float(input('Informe o valor do produto: '))
novo_valor = valor_produto - (valor_produto * 5/100)  # multiplicação e divisao tem a mesma ordem de precedencia
print(f'Preço do produto {valor_produto:.2f}\nNa liquidação, esse produto com desconto de 5%, sai por R${novo_valor:.2f}')
