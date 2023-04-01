#Um posto está vendendo combustíbel com a seguinte tabela de descontos:
# Alcool - até 20l desconto de 3% por litro, acima de 20l desconto de 5% por litro
# Gasolina - até 20l desconto de 4% por litro, acima de 20l 6% desconto por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustivel, codificado como A = Alcool
# e G = Gasolina , calcule eimprima o valor a ser pago pelo cliente sabendo que a gaso custa 2,5 e o A 1,9

tipo_combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ")
litros = float(input("Digite a quantidade de litros vendidos: "))

preco_gasolina = 2.5
preco_alcool = 1.9

if tipo_combustivel == 'G':
    if litros <= 20 and litros > 0:
        desconto = 0.04
        valor_sem_desconto = litros * preco_gasolina
        valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto)
        print(f"Valor a ser pago: R$ {valor_com_desconto}. Valor sem desconto: {valor_sem_desconto} e desconto de {valor_sem_desconto * desconto}")
    elif litros > 20:
        desconto = 0.06
        valor_sem_desconto = litros * preco_gasolina
        valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto)
        print(f"Valor a ser pago: R$ {valor_com_desconto}. Valor sem desconto: {valor_sem_desconto} e desconto de {valor_sem_desconto * desconto}")
    elif litros < 0:
        print('Quantidade inválida')
elif tipo_combustivel == 'A':
    if litros <= 20 and litros > 0:
        desconto = 0.03
        valor_sem_desconto = litros * preco_alcool
        valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto)
        print(f"Valor a ser pago: R$ {valor_com_desconto}. Valor sem desconto: {valor_sem_desconto} e desconto de {valor_sem_desconto * desconto}")
    elif litros > 20:
        desconto = 0.05
        valor_sem_desconto = litros * preco_gasolina
        valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto)
        print(f"Valor a ser pago: R$ {valor_com_desconto}. Valor sem desconto: {valor_sem_desconto} e desconto de {valor_sem_desconto * desconto}")
    elif litros < 0:
        print('Quantidade inválida')
else:
    print('Combustível inválido')
