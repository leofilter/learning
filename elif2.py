exercicio = int(input('Quantos minutos voce se exercita por dia? '))
if exercicio < 30:
    print('Voce deveria se exercitar mais!')
elif exercicio >= 30 and exercicio <= 60:
    print('Voce esta no caminho certo')
elif exercicio > 60 and exercicio <= 120:
    print('Voce e um(a) atleta')
else:
    print('Uau, voce se exercita muito!')
### ELSE = TODOS OS OUTROS
