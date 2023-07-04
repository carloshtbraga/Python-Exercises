# Exercício: Faça um algoritmo recursivo de soma. Esse algoritmo deve
# receber um número de parâmetro e deve somar todos os números
# antecessores a ele.


def soma(n):
    counter = 0
    for numero in range(1, n + 1):
        if numero % 2 == 0 and numero != 0:
            counter += 1
    print(counter)


soma(10)
