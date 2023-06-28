# exec 13
# ratings = [6, 8, 5, 9, 10]
# new = []

# for rating in ratings:
#     new.append(rating * 10)
# print(new)
# pythonico
ratings = [6, 8, 5, 9, 10]
new_ratings = [10 * rating for rating in ratings]

# exec 14
for rating in new_ratings:
    if (rating % 3) == 0:
        print(f"{rating} é multiplo de 3")


# exe 12
# number = 500
# counter = 1
# result = 1

# while counter <= number:
#     result = result * counter
#     counter += 1
# print(result)


# exercicio 8
salary = float(input("Digite o salário do funcionário: "))

position = ""
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"

# print("O funcionário é um %s" % position)