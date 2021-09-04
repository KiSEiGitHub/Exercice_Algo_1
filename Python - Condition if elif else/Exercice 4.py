# Exercice 4: Nature d'un triangle

if __name__ == '__main__':
    while True:
        try:
            AB = int(input("AB: "))
            BC = int(input("BC: "))
            AC = int(input("AC: "))
            break
        except ValueError:
            print("vous devez rentrer des nombres")

    if AB == AC and AC != BC:
        print('Le triangle ABC est: isocèle')

    elif AC == BC == AB:
        print('Le triangle est: équilatéral')

    elif AC ** 2 + BC ** 2 == AB ** 2:
        print("Ce triangle est rectangle")

    elif BC + AC == AB:
        print('Triangle quelconque')

    else:
        print("Ce n'est pas un triangle")