# Mostrar um texto com várias linhas em apenas um print, colocamos em 3 aspas DUPLAS
print(""" Boa tarde, gestores!

Informamos que, a partir desde momento por orientação jurídica, não faremos mais as antecipações de férias.
Ou seja, o funcionário só poderá gozar suas férias após tê-las direito adquirido (férias vencidas). 
Utilizávamos uma prática não condizente com a CLT, então a partir deste momento seguiremos a legislação trabalhista de forma objetiva.

A CLT trata que a antecipação de férias, antes de completado o período aquisitivo (12 meses), é possível  apenas nos casos de férias coletivas.  
Em casos realmente excepcionais (como casos de saúde), poderemos avaliar a situação juntamente com a direção podendo ser deferido ou não o pedido.""")

frase = 'Curso em Video Python' # contem 21 caracteres
print(frase)
print(frase.count('o')) # Função Count, conta quantos "o" minusculo ele encontrou

# Neste caso, testa quantos "O" MAIUSCULO aparecem
print(frase.count('O'))
# Como não aparecem nada, podemos converter a frase toda para MAIUSCULA.
print(frase.upper().count('O'))

frase2 = '   Curso em video Python   ' # contem 27 caracteres com os espaços
print(len(frase2)) # vai contar os espaços e aumentar o numero de caracteres.
# Para resolver
print(len(frase2.strip())) # com o metodos strip() que remove os espaços, volta a ter 21 caracteres

dividido = frase.split()
print(dividido[2] [3])
# Pega o dividido 2 que é Vídeo e mostra a letra 3
