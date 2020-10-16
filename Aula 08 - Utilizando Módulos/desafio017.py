from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2) # sem usar metodo importado
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
