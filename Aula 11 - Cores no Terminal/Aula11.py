# ver modulo colorize
"""
Método ruim de usar
print('\033[4;30;45mOlá, mundo')
"""

cores = {'limpa': '\033[m',
         'azul': '\033[36m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

nome = 'Josué'
print(f'Prazer em te conhecer {cores["azul"]}{nome}')
