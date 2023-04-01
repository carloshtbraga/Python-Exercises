#Programa que le uma matriz 3x3 digitada pelo usuário e conta quantos números pares existem na matriz, imprikindo na tela o resultado e a matriz


turma = []
for i in range(3):
    linha = []
    for ii in range(3):
       linha.append(int(input(f'Digite a nota [ {i}, {ii} ]: ')))
    turma.append(linha)
contador = 0
for i in turma:
    for ii in i:
        if ii % 2 == 0:
             contador += 1
print(f'O número de pares é: {contador}')
for i in turma:
    print(i)


