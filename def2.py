def imc (peso, altura):
    imc = peso/(altura**2)
    if  imc < 18.5:
        print('Magreza')
    elif imc >= 18.5 and imc <= 24.5:
        print('Normal')
    elif imc > 25.0:
        print('Sobrepeso')
    return
imc(74, 1.72)
print(imc)
