# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada
# 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que
# custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla
# contendo a quantidade de latas de tinta a serem compradas e o preço total
# a partir do tamanho de uma parede (em m²).


def calcular_quantidade_e_preco_pintura(area):
    cobertura_por_litro = 3
    capacidade_lata = 18
    preco_lata = 80.00

    quantidade_latas = area / cobertura_por_litro / capacidade_lata
    quantidade_latas = (
        int(quantidade_latas) + 1
        if quantidade_latas % 1 != 0
        else int(quantidade_latas)
    )
    preco_total = quantidade_latas * preco_lata

    return quantidade_latas, preco_total


print(calcular_quantidade_e_preco_pintura(500))
