total = 0
itens = 0
preco = 1
print ('Digite o preco dos produtos - ou 0 para encerrar')
while preco != 0:
    preco = float(input('Preço?: '))
    if preco != 0:
        total += preco
        itens +=1
print(':' * 35)
print('Quantidade de itens', itens)
print('Valor total da compra', total)
print(':' * 35)
