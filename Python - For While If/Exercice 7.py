from math import sqrt
from random import randint


def main():
    xb = randint(0, 100)
    yb = randint(0, 100)

    d = 11
    flag = 1

    while d > 10 and flag < 6:
        x = int(input("Abscisse: "))
        y = int(input("Ordonnée: "))

        flag += 1

        d = sqrt((x - xb) ** 2 + (y-yb) ** 2)

        if d <= 10:
            print("Bravo!")
        else:
            print("Trop lent")

if __name__ == '__main__':
    main()