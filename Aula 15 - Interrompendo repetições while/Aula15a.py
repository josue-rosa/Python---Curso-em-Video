soma = numero = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma vale {soma}')
