def main():
    print("Entrer 5 nombres")
    t = []
    for _ in range(5):
        n = int(input(">> "))
        if n < 10:
            t.append(n)

    print(f"Liste: {t}")


if __name__ == '__main__':
    main()