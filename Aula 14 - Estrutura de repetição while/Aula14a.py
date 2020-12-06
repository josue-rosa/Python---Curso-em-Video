# Exemplo 3 - PAR ou IMPAR

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:  # Se for Zero, finaliza o programa sem incluir o Zero na contagem
        if num % 2 == 0:  # Testa se for par ou impar
            par += 1  # Conta quantos numeros pares foram digitados
        else:
            impar += 1  # Conta quantos numeros impares foram digitados
print('Fim')
print(f'Você digitou {par} numero(s) par(es)')
print(f'Você digitou {impar} numero(s) impar(es)')


# exemplo 2 - Digitar N para sair
"""
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('fim')
"""

# Exemplo 1

"""
# Exemplo de semelhança entre os códigos.
# Ambos fazem a mesma coisa

for c in range(1, 11):
    print(c)
print('fim')


c = 1
while c < 11:
    print(c)
    c += 1
"""