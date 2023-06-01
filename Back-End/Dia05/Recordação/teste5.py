def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma(1,2,3,4))
print(soma(4,5,6))

def multiplicacao(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(multiplicacao(1,2,3,4))
print(multiplicacao(4,5,6))