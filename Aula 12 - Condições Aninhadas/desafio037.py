"""
Programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão

1 - para binário
2 - para octal
3 - para hexadecimal
"""

num = int(input('Digite um numero inteiro: '))
print('''
1 - Converter para BINÁRIO
2 - Converter para OCTAL
3 - Converter para HEXADECIMAL
''')
opcao = int(input('Informe a opção desejada '))

if opcao == 1:
    print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente')
