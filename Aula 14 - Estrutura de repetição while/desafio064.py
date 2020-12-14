
"""
programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag(999))
"""

numero = contador = soma = 0

while numero != 999:
    numero = int(input('Digite um valor [999 para Sair] '))
    if numero != 999:
        contador += 1
        soma += numero
print(f'Você informou {contador} numero[s].')
print(f'A soma do[s] valor[es] é {soma}.')
