#Faça um programa que pergunte em que turno vc estuda.
#Peça para digitar M matutino ou V vespertino e N noturno. Impra
#bom dia, boa tarde, boa noite ou valor invalido de acordo com o turno

n = input("Coloque o seu turno no formato M V OU N: ")
if(n=='M'):
    print('Bom dia')
elif(n=='V'):
    print('Boa tarde')
elif(n=='N'):
    print('Boa noite')
else:
    print('EROOOOOOU')
