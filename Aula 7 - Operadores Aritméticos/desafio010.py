# ler um numero e e calcular o seu valor em dolares
valor = float(input('Digite um valor em R$: '))
dolar = valor / 3.27

print(f'Com R$ {valor}, você pode comprar US$ {dolar:.2f} dolar(es)')
