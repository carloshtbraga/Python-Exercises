import random


def brinks():
    random_word = random.choice(["Leao", "Elefante", "Abutre", "Chacal"])

    scrambled_word = "".join(random.sample(random_word, len(random_word)))

    attempts = 3
    counter = 0
    for a in range(attempts):
        teste = input(f"Qual o animal {scrambled_word}?")

        if teste == random_word:
            print("Acertou uhuuuuuuuuuuul")
            break
        else:
            print("Errou, você tem 3 chances no total!")
            counter += 1
            if counter >= attempts:
                print("Acabaram as tentativas, u lose")
