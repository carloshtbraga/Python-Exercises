# O Hipermercado tabajara está com uma promoção de carnes
# Acima de 5kg, filé Duplo 4,90 o kg, Alcatra 5,90 o kg e Picanha 6.90
# Abaixo de 5kg: filé Duplo 5,80 o kg, Alcatra 6,80 o kg e Picanha 7.80

# Para atender todos os clientes, cada cliente poderá levar apenas um tipo de carne em promoção. Porém não há limites para a quantidade
# de carne por cliente. Se a compra usar o Cartão Tabajara o cliente receberá ainda 5% desconto no total da compra. Escreva um programa
# que peça o tipo e qtidade de carne comparada e a forma de pagamento ( C Cartao Taba - O outros ) gere um cupom com o tipo e quantidade
# de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar

tipoCarne = input("Coloque o tipo de carne: ")
qtdCarne = float(input("Coloque a quantidade da carne escolhida: "))
payment = input("Método de pagamento C para cartão Tabajara e O para outros ")

if tipoCarne == 'File Duplo':
    if qtdCarne > 5:
        precoKg = 4.90
    elif qtdCarne <= 5 and qtdCarne > 0:
        precoKg = 5.80

elif tipoCarne == 'Alcatra':
    if qtdCarne > 5:
        precoKg = 5.90
    elif qtdCarne <= 5 and qtdCarne > 0:
        precoKg = 6.80

elif tipoCarne == 'Picanha':
    if qtdCarne > 5:
        precoKg = 6.90
    elif qtdCarne <= 5 and qtdCarne > 0:
        precoKg = 7.80

precoTotal = qtdCarne * precoKg

if payment == 'C':
    precoC = precoTotal - (precoTotal * 0.05)
    print(f'Você comprou {qtdCarne} Kilos de {tipoCarne} por {precoKg} reais, ganhou {precoTotal * 0.05} totalizando {precoC}')
elif payment == 'O':
    print(f'Você comprou {qtdCarne} Kilos de {tipoCarne} por {precoKg} reais, totalizando {precoTotal}')
else:
    print('Pagamento inválido')

