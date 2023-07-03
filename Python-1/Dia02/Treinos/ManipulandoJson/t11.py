# Exercício 3:
# Dado um arquivo contendo estudantes e suas respectivas notas, escreva
# um programa que:

# lê todas essas informações;
# aplique um filtro, mantendo somente as pessoas que estão reprovadas;
# escreva seus nomes em outro arquivo.
# Considere que a nota miníma para aprovação é 6.

# Arquivo:

# Copiar
# Marcos 10
# Felipe 4
# José 6
# Ana 10
# Maria 9
# Miguel 5
# Exemplo saída:

# Copiar
# Felipe
# Miguel
# 🦜 A função split pode ser utilizada para dividir o nome em uma linha.
# Ex: line.split() -> ["Marcos", "10"].
recovery_students = []
with open("arquivo2.txt") as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recovery_students.append(student_grade[0])


with open("recuStudents.txt", mode="w") as recu_students_file:
    print(recovery_students)
    recu_students_file.writelines(recovery_students)
