kilosDePeixe = float(input('Coloque a quantidade de peixe em kilos: '))

limitePeixe = 50

excedenteDePeixe = kilosDePeixe - limitePeixe

if(kilosDePeixe <= 50):
    print(f'Se você pescou {kilosDePeixe} kilos de peixe você não paga multa pois pescou até {limitePeixe} kgs')
else:
    multaPorKilo = 4.00 
    multa = excedenteDePeixe * multaPorKilo
    print(f'Se você pescou {kilosDePeixe} kilos de peixe')
    print(f'E o limite do estado sem multa são {limitePeixe} kilos')
    print(f'Você precisa pagar {multaPorKilo} reais pra cada kilo de peixe que ultrapasse o limite')
    print(f'No seu caso, a multa é de {multa}')
