"""
programa que calcule a soma entre todos os números impares que são múltiplos de três
 e que se encontram no intervalo de 1 até 500.
"""

acumulador = contador = 0  # é a mesma coisa que dizer: x = 0, y = 0

for c in range(1, 501, 2):  # mostra os numeros impares
    if c % 3 == 0:  # testa os que são multiplos de 3
        acumulador += c  # guarda cada registro na variavel "acumulador"
        contador += 1
print(f'A soma de {contador} valores solicitados é {acumulador}')

"""
soma = 0  # acumulador
cont = 0  # contador. Geralmente soma +1
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de {cont} valores solicitados é {soma}')
"""