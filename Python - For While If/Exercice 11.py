from random import random


def main():
    c = 0
    n = 100000

    for _ in range(0, n):
        x = random()
        y = random()

        if x * x + y * y <= 1:
            c += 1

    print(4 * c / n)


if __name__ == '__main__':
    main()