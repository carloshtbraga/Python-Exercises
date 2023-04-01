# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores a b e c e fazer as consistencias, informando ao usuário as seguintes situações
#a) se o user der o valor de A igual a 0, a equação n é do segundo grau e o programa deve encerrar sem pedir b e c
#b) se o delta for negativo, a equação não possui raizes reais. Informe o usuário e encerre o programa
#c) se o delta calculado for igual a zero a equação possui apenas 1 raiz real, informe ao usuario
#d) se o delta for positivo a equação possui 2 raizes reais, informe o usuario
import math

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        print("A equação possui apenas uma raiz real")
    else:

        print("A equação possui duas raízes reais")
