def main():
    print("Entrer 5 nombres")
    t = [int(input(">> ")) for _ in range(5)]

    print("Entrer encore 5 nombres")
    t2 = [int(input(">> ")) for _ in range(5)]

    x = 0
    y = 0

    for i in range(len(t)):
        x += t[i] * t2[i]
        y += t2[i]

    print(f"Moyenne pondéré = {round(x / y, 2)}")


if __name__ == '__main__':
    main()