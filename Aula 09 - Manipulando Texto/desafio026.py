"""
Crie um programa que leia uma frase qualquer e mostre:
- Quantas vezes aparece a letra "A"

- Em que posição ela aparece a primeira vez

- Em que posição ela aparece a ultima vez
"""


frase = str(input('Informe uma frase: ')).strip().upper()
print(f"A letra A aparece {frase.count('A')} vezes na frase")
print(f"A letra A aparece a primeira vez na posição {frase.find('A')+1}")# Como começa na posição 0, acrescentei mais 1 para começar a contar a partir de 1
print(f"A ultima letra A apareceu na posição {frase.rfind('A')+1}")
