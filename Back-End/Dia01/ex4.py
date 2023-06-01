"""Faça um programa que leia três números inteiros e mostre o maior deles"""

n1 = float(input('Coloque um número'))
n2 = float(input('Coloque um número'))
n3 = float(input('Coloque um número'))
if (n2 > n1 and n2 > n3):   
    print(f'O maior número é {n2}')
elif(n3 > n2 and n3 > n1):   
    print(f'O maior número é {n3 }')
else:
    print(f'O maior número é {n1}')

 