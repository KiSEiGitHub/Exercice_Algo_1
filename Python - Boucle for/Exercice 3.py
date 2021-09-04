while True:
    try:
        somme = float(input("Somme: "))
        taux = float(input("Taux: "))
        annee = int(input("Année: "))
        break
    except ValueError:
        print("Vous devez rentrer un nombre")
for _ in range(annee):
    somme *= taux

print(f"Gaspard aura {round(somme, 2)}€ au bout de {annee} ans")