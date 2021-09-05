from random import random


def main():
    c = 0
    n = 10000

    for _ in range(0, n):
        x = random() * 2
        y = random() * 4

        if y <= x ** 2:
            c += 1
    print(8 * c / n)

if __name__ == '__main__':
    main()