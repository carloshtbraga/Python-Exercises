def ricardo(a, b):
    if b == 2:
        print(f'O número {a} duplicado é {a*b}')
    elif b == 3:
        print(f'O número {a} triplicado é {a*b}')
    elif b == 4:
        print(f'O número {a} quadruplicado é {a*b}')
    else:
        print(f'O valor do segundo parametro deve ser 2, ou 3 ou 4')

ricardo(2,4)