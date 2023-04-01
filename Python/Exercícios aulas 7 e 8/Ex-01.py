def carlos(array):
    maior = 0
    soma = 0
    for i in array:
        soma += i
        if i > maior:
            maior = i
    media = soma / len(array)
    print(f'O maior número é {maior}, a soma é {soma} a média é {media} e tem {len(array)} números nesse array')


carlos([4, 6, 8, 2, 10, 8, 10, 12, 45]) 


