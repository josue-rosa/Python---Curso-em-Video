
operador = 0

while True:
    print('-' * 45)
    numero = int(input('Você deseja ver a tabuada de qual valor? '))
    if numero > 0:
        while operador < 10:
            operador += 1
            print(f'{numero} x {operador:2} = {numero * operador}')
    else:
        break

