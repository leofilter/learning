trabalho = input('Voce deve trabalhar hoje? ')
dia = input('O dia esta bonito? ')
preguica = input('Voce esta com preguica? ')
### VARIAVEIS DO LOOP
if trabalho == 'sim':
    print('E uma pena')
elif trabalho == 'nao':
    print('Aproveite o dia')


if dia == 'sim' and trabalho == 'nao':
    print('Aproveite para caminhar')
elif dia == 'nao' and trabalho == 'nao':
    print('Aproveite e assista um filme')

if preguica == 'sim' and trabalho == 'nao':
    print('Aproveita e dorme mais')
elif preguica == ' nao' and trabalho == 'nao':
    print('Que tal estudar Python?')

