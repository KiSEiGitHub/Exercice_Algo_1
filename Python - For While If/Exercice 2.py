def main():
    feuille = 0.1
    x = 0

    while feuille <= 324000:
        x += 1
        feuille *= 2

    print(f"Il faudra plier la feuille {feuille} fois")


if __name__ == '__main__':
    main()