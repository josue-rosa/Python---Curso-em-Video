"""
Programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida.

- media abaixo de 5.0: 
reprovado
- media entre 5.0 e 6.9: 
recuperação
- media 7.0 ou superior:
aprovado
"""
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi {media}. Por isso, você está REPROVADO')
elif media <= 6.9:
    print(f'Sua média foi {media}. Você ficou em RECUPERAÇÃO')
else:
    print(f'Sua média foi {media}. Você está APROVADO')
