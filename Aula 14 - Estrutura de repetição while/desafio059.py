"""
Leia dois valores e mostre um menu na tela

[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa

seu programa deverá realizar a operação solicitação em cada caso
"""

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

opcao = int(input("""
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa """))

while opcao != 5:
    if opcao == 1:
        print(f'A soma dos numeros é: {num1 + num2}')
        break
    elif opcao == 2:
        print(f'A multiplicação dos numeros é: {num1 * num2}')
        break
    elif opcao == 3:
        if num1 > num2:
            print(f'O Maior numero é o {num1}')
        else:
            print(f'O Maior numero é o {num2}')
        break
    elif opcao == 4:
        num1 = int(input('Digite o primeiro numero de novo: '))
        num2 = int(input('Digite o segundo numero de novo: '))
        break
