def ricardo(a, *args):
    for b in args:
        if b == 2:
            print(f'O número {a} duplicado é {a * b}')
        elif b == 3:
            print(f'O número {a} triplicado é {a * b}')
        elif b == 4:
            print(f'O número {a} quadruplicado é {a * b}')
        else:
            print(f'O valor do parâmetro deve ser 2, 3 ou 4. Valor fornecido: {b}')

ricardo(2)                # Saída: O valor do parâmetro deve ser 2, 3 ou 4. Valor fornecido: 
ricardo(2, 2)             # Saída: O número 2 duplicado é 4
ricardo(2, 3)             # Saída: O número 2 triplicado é 6
ricardo(2, 4)             # Saída: O número 2 quadruplicado é 8
ricardo(2, 5)             # Saída: O valor do parâmetro deve ser 2, 3 ou 4. Valor fornecido: 5
ricardo(2, 3, 4)          # Saída: O número 2 triplicado é 6, O número 2 quadruplicado é 8
ricardo(2, 2, 3, 4, 5)    # Saída: O número 2 duplicado é 4, O número 2 triplicado é 6, O número 2 quadruplicado é 8, O valor do parâmetro deve ser 2, 3 ou 4. Valor fornecido: 5
