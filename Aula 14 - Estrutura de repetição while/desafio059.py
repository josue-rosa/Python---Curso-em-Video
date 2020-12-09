"""
Leia dois valores e mostre um menu na tela

[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa

seu programa deverá realizar a operação solicitação em cada caso
"""
from time import sleep

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] novos números
    [5] sair ''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} + {num2} é {soma}')
    elif opcao == 2:
        multi = num1 * num2
        print(f'A multiplicação entre {num1} x {num2} é {multi}')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é o maior')
        else:
            print(f'{num2} é o maior')
    elif opcao == 4:
        num1 = int(input('Digite seu primeiro novo valor. '))
        num2 = int(input('Digite seu segundo novo valor. '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa!')


# Meu programa

"""
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

opcao = int(input('''
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa '''))

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
"""