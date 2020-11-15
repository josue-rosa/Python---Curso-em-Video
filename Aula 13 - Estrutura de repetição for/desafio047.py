"""programa que mostre na tela dos os numeros pares que estão no
intervalo entre 1 e 50."""

for c in range(1, 51):
    resto = c % 2
    if resto == 0:
        print(c)
