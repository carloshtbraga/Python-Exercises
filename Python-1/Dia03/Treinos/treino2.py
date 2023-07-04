import time


def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f"Array 1: {number1}")
        for number2 in array2:
            print(f"Array 2: {number2}")
            result.append(number1 * number2)
            number_of_iterations += 1

    print(f"{number_of_iterations} iterações!")
    return result


meu_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 3, 4]
inicio = time.time()
multiply_arrays(meu_array, meu_array)
fim = time.time()

# Tempo total de execução
tempo_total = fim - inicio
print(f"Tempo de execução: {tempo_total} segundos")
