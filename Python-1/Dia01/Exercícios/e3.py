# Exercício 3: Faça um programa que, dado um valor n qualquer,
# tal que n > 1,# imprima na tela um quadrado
# feito de asteriscos de lado de tamanho n. Por exemplo:

n = int(input('Digite um número maior que 1: '))
for each in range(n):
    print(n * '*', each)
