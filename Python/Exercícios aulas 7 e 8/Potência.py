base = int(input("Digite um número inteiro para a base: "))
expoente = int(input("Digite um número inteiro para o expoente: "))
acumulador = 1
if base == 0 and expoente == 0:
    print('Sacaneou né, 0 elevado a 0 é infinito')
elif expoente < 0:
    while expoente < 0:
        acumulador *= base
        expoente += 1
    print(f'O resultado é {1/acumulador}')
else:
    while expoente > 0:
        acumulador *= base
        expoente -= 1
    print(f'O resultado é {acumulador}')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                