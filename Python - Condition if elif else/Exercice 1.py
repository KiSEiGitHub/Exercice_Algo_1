if __name__ == '__main__':
    while True:
        try:
            AB = int(input("AB: "))
            BC = int(input("BC: "))
            AC = int(input("AC: "))
            break
        except ValueError:
            print("Vous devez rentrer un nombre")

    if AB == AC and AC != BC:
        print('Le triangle ABC est: isocèle')
        print("Parce que: AB = AC")
    elif AC == BC == AB:
        print('Le triangle est: équilatéral')
        print("Parce que: Tous les côtés ont la même longeur")
    else:
        print(f"Le triangle n'est ni isocèle, ni équilatéral")