turma = []

for i in range(3):
    linha = []
    for ii in range(5):
       linha.append(int(input(f'Digite a nota [ {i}, {ii} ]: ')))
    turma.append(linha)
print(turma)
media = 0
for i in turma:
    for ii in i:
        media = media + ii
media = media / (len(turma) * len(i))
print(media)
