"""escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar  80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7 por cada km acima do limite
"""

velocidade = float(input('Informe a velocidade do carro em Km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado. Você deve pagar R${multa:.2f}')
