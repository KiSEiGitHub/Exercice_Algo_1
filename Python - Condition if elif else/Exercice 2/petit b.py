# Exercice 2: Triangle rectangle
# petit b

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