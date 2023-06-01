def multiplicar_parametros(a, b):
    numeros_permitidos = [2, 3, 4, 5, 6, 7, 8]  # Lista de números permitidos para multiplicação
    if b in numeros_permitidos:
        resultado = a * b
        print(f'O número {a} multiplicado por {b} é {resultado}')
    else:
        print(f'O valor do parâmetro deve ser um dos seguintes números: {numeros_permitidos}')

multiplicar_parametros(2, 3) 
multiplicar_parametros(4, 5)   
multiplicar_parametros(3, 7)  
multiplicar_parametros(5, 9)   