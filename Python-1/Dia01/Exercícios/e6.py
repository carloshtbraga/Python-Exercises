# Exercício 6: Crie uma função que receba os três lado de um triângulo e#
# informe qual o tipo de triângulo formado ou "não é triangulo", caso
# não seja possível formar um triângulo.


def wichTriangle(a, b, c):
    if a + b < c or c + b < a or c + a < b:
        print("Não é um triangulo essa porra!")
    elif a == b == c:
        print("Triângulo Equilátero: três lados iguais")
    elif a == b or c == b or c == a:
        print("Triângulo Isósceles: quaisquer dois lados iguais;")
    else:
        print("Triângulo Escaleno: três lados diferentes")


wichTriangle(3, 3, 3)
