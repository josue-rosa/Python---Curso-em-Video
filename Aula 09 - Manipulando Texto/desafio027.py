"""
Faça um programa que leia o nome completo de uma pessoa e mostrando em seguida o primeiro e o ultimo nome separadamente

Ex: Ana Maria de Souza
Primeiro: Ana
Ultimo: Souza
"""

nome = str(input('Digite seu nome completo: ')).strip().title()
Splitter_name = nome.split()

print('Olá. Prazer em te conhecer')
print(f'Seu primeiro nome é {  Splitter_name[0]}')
print(f'Seu último nome é {Splitter_name[len(Splitter_name)-1]}')
