# Faça um programa que leia e valide as seguintes informações
#a- Nome: maior opu igual 3 caracters
#b- Idade: entre 0 e 150
#c- Salário: maior que 0
#d- Sexo: f ou m
#e- Estado Civil: s, c, v, d
nome = input('Coloque seu nome: ')
idade = int(input('Coloque sua idade: '))
salario = float(input('Coloque seu nome: '))
sex= input('Coloque seu sexo: ')
civil = input('Coloque seu Estado Civil: ')
validSex = sex =='f' or sex =='m' or sex == 'F' or sex =='M'
validCivil = civil =='s' or civil == 'c' or civil == 'v' or civil ==  'd'
validation = len(nome) >= 3 and idade >=0 and idade <=150 and salario > 0 and sex == true and civil == true
if validation:
    print('Você está logado')
else:
    print('Alguma informação digitada erroneamente')


