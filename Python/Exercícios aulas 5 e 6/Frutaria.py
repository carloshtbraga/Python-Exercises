# Uma frutaria está vendendo frutas com a seguinte tabela de preços:
# Até 5kg, Morango 2,50 e maçã 1,80
# Acima de 5kg , morango 2,20 e maçã 1,50

# Se o cliente comprar mais de 8kg em frutas ou o total da compra ultrapassar 25,00, receberá ainda um desconto de 10% no total.
# Escreva um algoritmo para ler a quantidade em kg de morangos e maça e escreva o valor a ser pago

kgMorango = float(input("Coloque a quantidade de morango em Kgs: "))
kgMaca = float(input("Coloque a quantidade de maçã em Kgs: "))

if kgMorango <= 5:
    precoMorango = 2.5
else:
    precoMorango = 2.2

if kgMaca <= 5:
    precoMaca = 1.8
else:
    precoMaca = 1.5

valorTotal = (kgMorango * precoMorango) + (kgMaca * precoMaca)

if kgMorango + kgMaca > 8:
    valorTotal = valorTotal  - (valorTotal * 10 / 100)

print(f'Quantidade comprada de morango: {kgMorango}, valor por kilo: {precoMorango}')
print(f'Quantidade comprada de maca: {kgMaca}, valor por kilo: {precoMaca}')
print(f'Valor total: {valorTotal}')
