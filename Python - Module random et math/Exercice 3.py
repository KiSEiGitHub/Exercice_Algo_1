from random import randint

def main():
    tortue = 0
    lapin = 0

    for _ in range(1000):
        gagner = 0
        c = 0
        while gagner == 0:
            d = randint(1, 6)
            if d == 6:
                gagner = 1
                lapin += 1
            else:
                c += 1
                if c == 6:
                    gagner = -1
                    tortue += 1

    print(f"Tortue: {tortue}")
    print(f"Lapin: {lapin}")



if __name__ == '__main__':
    main()