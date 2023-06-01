"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de renda, que depende do 
salário bruto(Conforme tabela abaixo) e 3% para o sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado(é 
a empresa que deposita). O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% imprima na tela as informações , dispostas confore o exemplo abaixo. No exemplo o
valor da hora é 5 e a quantidade de hora é 220

Salário Bruto:( 5 * 200) : R$ 1100,00
(-)IR (5%)  : r$ 55,00
(-)INSS(10%)  110,00
FGTS (11%)   : R$ 121,00
Total de descontos R$ 165,00
Salário Líquido : R$ 935,00

"""
horas=int(input('Coloque o número de horas trabalhadas'))
valorHora=float(input('Coloque o valor da sua hora'))

salarioBruto = horas * valorHora
fgts = salarioBruto * 0.11
inss = salarioBruto * 0.10
ir= 0
totalDescontos = ir + inss
salarioLiquido = salarioBruto - totalDescontos
if salarioBruto <= 900:
    ir = 0
    print(f'Com o salário de {salarioBruto} o IR é zerado, o inss:{inss} e o fgts:{fgts} logo seu salário líquido é de {salarioLiquido}')
elif salarioBruto <= 1500:
    ir = salarioBruto * 0.05
    totalDescontos = ir + inss
    print(f'Com o salário de {salarioBruto} o IR é {ir}, o inss:{inss} e o fgts:{fgts} logo seu salário líquido é de {salarioLiquido}')
elif salarioBruto <= 2500:
    ir = salarioBruto * 0.1
    totalDescontos = ir + inss
    print(f'Com o salário de {salarioBruto} o IR é {ir}, o inss:{inss} e o fgts:{fgts} logo seu salário líquido é de {salarioLiquido}')
else:
    ir = salarioBruto * 0.2
    totalDescontos = ir + inss
    print(f'Com o salário de {salarioBruto} o IR é {ir}, o inss:{inss} e o fgts:{fgts} logo seu salário líquido é de {salarioLiquido}')
