metragem = float(input('Coloque a quantidade de metros quadrado da casa: '))
qtdLataEmLitro = 18
umLitroFaz = 3
lataFaz = qtdLataEmLitro * umLitroFaz
lataPreco = 80.00
qtdLataUsada = round(metragem / lataFaz + 0.5)
valorFinal = round(qtdLataUsada * lataPreco, 2)

print(f'Se a casa tem {metragem} metros, um litro de tinta faz {umLitroFaz} metros, uma lata tem {qtdLataEmLitro} litros e cada lata custa {lataPreco}. Voce usará {qtdLataUsada} lata(s) e isso custará {valorFinal}')


