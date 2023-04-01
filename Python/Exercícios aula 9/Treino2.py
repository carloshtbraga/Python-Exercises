matriz = [[8,8,9,7], [10,6,7,8], [9,10,7,8], [10,10,10,10]]

media = 0
for i in matriz:
    for ii in i:
        media = media + ii
media = media / (len(matriz) * len(i))
print(media)
