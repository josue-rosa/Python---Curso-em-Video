from math import radians, sin, cos, tan

angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem COSSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem TANGENTE de {tangente:.2f}')
