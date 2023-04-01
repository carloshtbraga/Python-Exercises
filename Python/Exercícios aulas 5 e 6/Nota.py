#Faça um programa que peça uma nota entre zero e dez. Mostre uma mensagem caso o valor seja inválido
#e continue pedindo até que o usuário informe um valor válido

nota = float(input('Coloque uma nota: '))
while nota >=0 and nota <=10:
    nota = float(input('Coloque uma nota: '))

print('Valor inválido')
