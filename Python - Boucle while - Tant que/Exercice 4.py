def main():
    livret = float(input("Argent: "))
    taux = float(input("Taux d'intérêt en pourcentage: "))
    annee = 0
    while livret <= 1700:
        livret *= taux
        annee += 1
    print(f"Il pourra l'avoir en {annee} ans")



if __name__ == '__main__':
    main()