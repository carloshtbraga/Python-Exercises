numero = int(input('Coloque um número inteiro entre 1 e 10: '))
while numero < 1 or numero > 10:
    numero = int(input('Coloque um número inteiro entre 1 e 10 PORRA: '))
contador = 1
while contador <= 10:
    print(f'{numero} * {contador} = {numero * contador}')
    contador += 1