'''
num = int(input('Informe um numero: '))
n = str(num)

print(f'Analisando seu numero {num}')

print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

# No exemplo acima exibirá um problema quando colocar numeros menores.
# Ex: 123 ou 12 ou 5
# Só funcionará quando o numero tiver 4 digitos. Ex: 1234

'''

# Outra Solução
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'milhar: {m}')
