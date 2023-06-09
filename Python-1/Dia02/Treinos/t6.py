# Escreva um programa que receba vários números naturais e calcule a soma
# desses valores. Caso algum valor da entrada seja inválido (por exemplo uma
# letra), uma mensagem deve ser exibida na saída de erros no seguinte
# formato: “Erro ao somar valores, {valor} é um valor inválido”. Ao
# final, você deve imprimir a soma dos valores válidos.

numbers = input("Coloque alguns números separados por espaço: ")


def soma(numbers):
    separatedNumbers = numbers.split(" ")
    counter = 0
    for number in separatedNumbers:
        if not number.isdigit():
            print(f"Erro ao somar valores, {number} não é um dígito.")
            break
        else:
            counter += int(number)
    print(f"Os números foram {separatedNumbers} e a soma dos "
          f"seus números é {counter}")


soma(numbers)
