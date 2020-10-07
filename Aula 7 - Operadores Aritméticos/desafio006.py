# ler um numero e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um numero: '))

print(f'Dobro: {n1*2}')
print(f'Triplo: {n1*3}')
print(f'Raiz Quadrada: {n1**(1/2):.2f}')
print(f'Outra forma de fazer raiz quadrada {pow(n1,(1/2)):.2f}')
