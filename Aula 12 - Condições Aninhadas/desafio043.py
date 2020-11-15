"""programa que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- acima de 40: Obesidade Mórbida
"""

peso = float(input('Informe o seu peso em Kg: '))
altura = float(input('Informe a sua altura em M: '))

imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25: # ou 18.5 <= imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
