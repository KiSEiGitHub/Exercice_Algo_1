def main():
    appartement = 100000
    for _ in range(1, 11):
        appartement *= 1.01
    print(f"Au bout de 10 ans l'appartement vaudra {round(appartement, 2)}€")

    annee = 0
    while appartement < 200000:
        annee += 1
        appartement *= 1.01

    print(f"L'appartement aura doubler de prix au bout de {annee} ans")



if __name__ == '__main__':
    main()