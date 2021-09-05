from random import randint


def main():
    only_6 = 0
    n = int(input("Nombre de lancers ?: "))
    for _ in range(n):
        d = randint(1, 6)
        d2 = randint(1, 6)
        if d == 6 and d2 == 6:
            only_6 += 2

    print(f"Il y a eu {only_6} six")
    print(f"Somme total = {only_6 * 6}")


if __name__ == '__main__':
    main()