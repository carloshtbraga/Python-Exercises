"""
Faça um programa que pede duas notas de um aluno, em seguida ele deve calcular a média do aluno
7 aprovado, 4 pra baixo reprovado e entre 5 e 7 aprovado

"""
nota1 = float(input('Coloque a primeira nota: '))
nota2 = float(input('Coloque a segundaa nota: '))
media = (nota1 + nota2) / 2
if(media >= 7):
    print(f"Aprovado com a média {media}")
elif(media < 4 ):
    print(f'Reprovado =(( sua média foi {media}')
else:
    print(f"Recuperação!!!!! Sua média é {media}")
    