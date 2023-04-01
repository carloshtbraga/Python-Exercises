sudeste = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
notas = [5.4, 7.5, 8.6, 10]
print('Estados do sudeste: ')
for x in range(len(sudeste)):
    print(f'{x+1} {sudeste[x]}')
print('-' * 30)
print('Notas: ')
for n in notas:
    print(n)