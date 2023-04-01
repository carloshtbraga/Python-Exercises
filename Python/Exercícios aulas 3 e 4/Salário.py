#Sálario
valorHora = float(input('Coloque o valor que você recebe por hora trabalhada: '))
horasTrabalhadas = float(input('Coloque o número de horas trabalhadas: '))
salarioBruto = valorHora * horasTrabalhadas
ir = 0.11
inss = 0.08
sindicato = 0.05
descontos = (salarioBruto * ir) + (salarioBruto * inss) + (salarioBruto * sindicato)
salarioLiquido = salarioBruto - descontos

print(f'Se você ganha {valorHora} por hora e trabalha {horasTrabalhadas} horas por dia, seu sálario BRUTO é de {salarioBruto} reais, os descontos tem o valor de {descontos} e o sálario líquido é de {salarioLiquido}')
 
