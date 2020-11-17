"""Programa que leia o primeiro termo e a razão de uma PROGRESSÃO
ARITMÉTICA. No final, mostre os 10 primeiros termos dessa progressão."""

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = primeiro_termo + (10 - 1) * razao  # calcular enésimo
for c in range(primeiro_termo, decimo + razao, razao):
    print(c, end=' -> ')
print('FINISH')
