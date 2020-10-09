# ler largura e altura de uma parede em metros e calcule a sua area e a quantidade de tinta
# necessária para pintar, cada litro de tinta pinta uma area de 2m².

largura = float(input('largura da parede em Metros: '))
altura = float(input('altura da parede em Metros: '))
area = largura*altura
litro_tinta = area/2
print(f'Area da parede: {area} m²')

print(f'Você precisará de {litro_tinta:.0f} litro(s) de tinta')
