
"""
programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se
ele quer ou não continuar a digitar valores
"""

resp = 'S'

media = quantidade = soma = maior = menor = 0

while resp in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

media = soma / quantidade

print(f'Você informou {quantidade} numeros')
print(f'A médias dos valores informados é {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
