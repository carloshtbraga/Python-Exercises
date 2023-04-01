n = int(input("Quantos números você quer digitar? "))
if n <= 1:
    print("Por favor, digite um número maior do que 1.")
else:
    maior = float(input("Digite o 1º número: "))
    soma = maior
    i = 2
    while i <= n:
        num = float(input(f"Digite o {i}º número: "))
        soma += num
        if num > maior:
            maior = num
        i += 1
    media = soma / n
    print(f"O maior número é {maior}.")
    print(f"A soma dos números é {soma}.")
    print(f"A média dos números é {media}.")
