"""
Programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- se é a hora de ele se alistar
- se já passou do tempo de se alistar

seu programa também devera mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date

ano_jovem = int(input('Informe seu ano de nascimento: '))
ano = date.today().year - ano_jovem
if ano < 18:
    print(f'Você tem {ano} anos')
    print('Você ainda vai se alistar')
    print(f'Faltam {18 - ano} para o alistamento')
elif ano == 18:
    print(f'Você tem {ano} anos')
    print('é hora de você se alistar')
else:
    print(f'Você tem {ano} anos')
    print(f'Já passou do tempo de se alistar. \nVocê Você deveria ter se alistado há {ano - 18} anos')
