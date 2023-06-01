# As organizações teste resolveram dar um aumento de salário aos seus calaboradores e lhe cotnrataram para desenvolver um programa que irá calcular os reajustes. Faça um programa que receba um salário e o reajuste seguindo o seguinte critério:
# Salários até 280,00 ( incluído ): aumento de 20%
# Salários entre 280,00 e 700,00: aumento de 15%
# Salários entre 700,00 e 1500,00: aumento de 10%
# Salários acimade 1500 ( incluído ): aumento de 5%
# O salário antes do reajuste.O percentual de aumento aplicado.O valor do aumentoo novo salário, após o aumento.

salario = float(input('Coloque o seu salário: '))
if salario <= 280:
    aumento = salario * 0.20
    total = salario + aumento
    print(f'O seu salário é {salario}, o aumento foi de {aumento} e o total ficou em {total}')
elif salario > 280 and salario <=700:
    aumento = salario * 0.15
    total = salario + aumento
    print(f'O seu salário é {salario}, o aumento foi de {aumento} e o total ficou em {total}')
elif salario > 700 and salario <=1500:
    aumento = salario * 0.10
    total = salario + aumento
    print(f'O seu salário é {salario}, o aumento foi de {aumento} e o total ficou em {total}')
else:
    aumento = salario * 0.05
    total = salario + aumento
    print(f'O seu salário é {salario}, o aumento foi de {aumento} e o total ficou em {total}')
