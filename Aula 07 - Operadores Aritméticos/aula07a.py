# testes

# nome = input('Qual o seu nome? ')
# print(f'Prazer em te conhecer {nome:*^30}')  # f-string literal

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print(f'A soma vale {n1+n2} e', end=" >>> ")  # "end=" " tirar a quebra de linha e colocar na mesma linha
print(f'a multiplicação é {n1*n2}.')
print(f'A potenciação é {n1**n2}')
print(f'A divisao é {n1/n2:.2f}')  # ":.2f" e para colocar duas casas decimais
print(f'A divisao inteira é {n1//n2}')
print(f'O resto da divisao é {n1%n2}')
