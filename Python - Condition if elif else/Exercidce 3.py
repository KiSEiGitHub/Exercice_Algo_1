# Exercice 3: Conditions d'existence d'un triangle - Inégalité triangulaire

if __name__ == '__main__':
    while True:
        try:
            AB = int(input("AB: "))
            BC = int(input("BC: "))
            AC = int(input("AC: "))
            break
        except ValueError:
            print("vous devez rentrer des nombres")

    if BC + AC != AB:
        print("Inégalité triangulaire")
        print("Parce que: BC + AC n'est pas égal à AB")
    else:
        print("Triangle possible")