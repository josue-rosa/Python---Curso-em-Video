nome = str(input('Informe seu nome: ')).title()
if nome == 'Josué' or nome == 'Davi':
    print(f'Que nome lindo! Bem-vindo {nome}!')
elif nome in 'Paloma Jéssica Ana':
    print(f'Você é a pessoa que cuida do Davi. Bem-vinda {nome}')
else:
    print(f'Prazer em te conhecer {nome}')
