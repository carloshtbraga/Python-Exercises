number = int(input('Insira um número inteiro: '))
ultimo = 1
penultimo =1
if number == 1 or number == 2:
    print('O valor fibonacci para 1 ou 2 números é sempre 1')
else:
    cont = 3
    while cont <= number:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo + penultimo
    print(f'O valor do termo fibonacci é {termo}')
