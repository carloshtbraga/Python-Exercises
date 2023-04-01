#Programa que cria uma matriz linhas x colunas preenchida com zeros

l=int(input('Digite a o número de linhas: '))
c=int(input('Digite a o número de colunas: '))
matriz = []
for i in range(l):
    linha = []
    for ii in range(c):
        linha.append(0)
    matriz.append(linha)
print(matriz)

#ou

l=int(input('Digite a o número de linhas: '))
c=int(input('Digite a o número de colunas: '))
matriz = []
for i in range(l):  
    matriz.append([0] * c)
print(matriz)
for i in range(c):
    print(matriz[i])