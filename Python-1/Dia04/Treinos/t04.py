# Exercício: Faça um algoritmo recursivo de soma. Esse algoritmo
# deve receber um número de parâmetro e deve somar todos os números
# antecessores a ele.


def soma_recursiva(num):
    if num == 0:  # Caso base: quando o número é zero, a soma é zero.
        return 0
    else:
        return num + soma_recursiva(
            num - 1
        )  # Chamada recursiva diminuindo o número em 1 a cada chamada


# Exemplo de uso:
resultado = soma_recursiva(5)
print(f"A soma dos números antecessor {resultado}")
