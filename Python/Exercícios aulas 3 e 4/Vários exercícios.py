

#Celsius to Fahrenheit

#celsius = float (input ('Digite uma temperatura em Celsius: '))

#print ( 'Levando em consideração a temperatura de ' + str(celsius) + ' Celsius, o resultado em fahrenheit é : ' + str(celsius * 1.8 +32))
#print(f'Levando em consideração a temperatura de {celsius} Celsius, o resultado em Fahrenheit é: {celsius * 1.8 + 32}')


#Calculadora de IMC

#peso = float (input ('Digite um peso em kilos: '))
#altura = float (input ('Digite sua altura em metros: '))
#print (f'O seu IMC é: {peso / altura**2}')


# Devolve em segundos os valores adicionados

#dias = float(input ('Digite o número de dias: ')) * 24 * 60 * 60
#horas = float(input ('Digite o número de horas: ')) * 60 * 60
#minutos = float(input ('Digite o número de minutos: ')) * 60
#segundos = float(input ('Digite o número de segundos: '))

#print (dias + horas + minutos + segundos)

# Calcula o desconto e preço final após recebendo o preço e % de desconto

preco = float(input('Coloque o preço do produto: '))
desconto = float(input('Coloque o desconto em % do produto: '))
desconto_em_reais = preco * desconto / 100
preco_com_desconto = preco - desconto_em_reais
print(f'Sendo o preço {preco} e o desconto de {desconto}%, esse desconto tem o valor de {desconto_em_reais} e o preço final do produto fica em {preco_com_desconto}')


