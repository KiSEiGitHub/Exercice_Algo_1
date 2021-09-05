from random import randint


def main():
    mise = int(input("Mise: "))

    d = randint(1, 6)
    d2 = randint(1, 6)

    if d == d2:
        print("Vous avez gagner")
        print(f"vous avez fait un double {d}")
        print(f"Vous récupérer {mise + d * 2}€")
    else:
        print("vous avez perdu")


if __name__ == '__main__':
    main()