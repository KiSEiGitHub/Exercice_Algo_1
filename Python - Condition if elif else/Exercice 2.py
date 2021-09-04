# Exercice 2: Triangle rectangle

def a():
    while True:
        try:
            AB = int(input("AB: "))
            BC = int(input("BC: "))
            if AB > BC:
                while True:
                    print('AB doit êtres plus petit que BC')
                    AB = int(input("AB: "))
                    break
            AC = int(input("AC: "))
            break
        except ValueError:
            print("vous devez rentrer un nombre")

    Rectangle = AC ** 2 + BC ** 2
    if Rectangle == AB ** 2:
        print("Ce triangle est rectangle")
    else:
        print("Ce triangle n'est pas rectangle")

def b():
    while True:
        try:
            AB = int(input("AB: "))
            BC = int(input("BC: "))
            AC = int(input("AC: "))
            break
        except ValueError:
            print("vous devez rentrer un nombre")

    Rectangle = AC ** 2 + BC ** 2
    if Rectangle == AB ** 2:
        print("Ce triangle est rectangle")
    else:
        print("Ce triangle n'est pas rectangle")

dico = {
    '1': a,
    '2': b
}
if __name__ == '__main__':
    user_choix = input("1 / 2 : ")
    fonc = dico.get(user_choix)
    fonc()