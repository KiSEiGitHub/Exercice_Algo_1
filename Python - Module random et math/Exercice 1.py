from random import randint

def main():
    point = 0

    for _ in range(10):
        a = randint(1, 10)
        b = randint(1, 10)
        print(f"{a} * {b} ?")

        c = int(input(">> "))

        if c == a * b:
            print("+1")
            point += 1
        else:
            print('-1')
            point -= 1

    print(f"Vous avez {point} points")


if __name__ == '__main__':
    main()