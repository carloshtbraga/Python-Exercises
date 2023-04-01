primos = []
primos = primos + [9]
primos = [2, 3] + primos
primos = primos[:2] + [5, 7] + primos[2:]
primos += [11]
print(primos)