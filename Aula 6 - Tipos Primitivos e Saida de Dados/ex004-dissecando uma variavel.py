algo = input('Digite algo: ')

print(f'O tipo primitivo disso é {type(algo)}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É numerico? {algo.isnumeric()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está totalmente em MAIUSCULO? {algo.isupper()}')
print(f'Está totalmente em minusculo? {algo.islower()}')
print(f'Está capitalizado? {algo.istitle()}')
print(f'Só tem espaços? {algo.isspace()}')
