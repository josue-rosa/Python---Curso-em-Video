"""
Programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SENIOR
- acima: MASTER
"""

from datetime import date

ano_atleta = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano_atleta

if idade <= 9:
    print(f'Você tem {idade} ano(s). Categoria MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} ano(s). Categoria INFANTIL')
elif idade <= 19: 
    print(f'Você tem {idade} ano(s). Categoria JUNIOR')
elif idade <= 20:
    print(f'Você tem {idade} ano(s). Categoria SENIOR')
else:
    print(f'Você tem {idade} ano(s). Categoria MASTER')
