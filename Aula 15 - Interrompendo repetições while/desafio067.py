"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    print('-' * 45)
    numero = int(input('Você deseja ver a tabuada de qual valor? '))
    print('-' * 45)
    if numero > 0:
        for c in range(1, 11):
            print(f'{numero} x {c:2} = {numero * c}')
    else:
        print('Programa encerrado')
        break
