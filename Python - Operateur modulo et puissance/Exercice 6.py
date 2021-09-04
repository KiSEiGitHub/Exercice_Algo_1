n = 14

while n > 0:
    a = ""
    while a not in [1, 2, 3]:
        a = int(input("Combien d'allumettes ?: "))
    n -= a
    if a == 0:
        print("vous avez perdu")
        break
    else:
        print(f"{n} allumettes restante")
        if n % 4 == 3:
            b = 2
        elif n % 4 == 2 or n % 4 != 0:
            b = 1
        else:
            b = 3
        print(f"L'ordi a pris {b} allumettes")
        n -= b
        print(f"{n} allumettes restante")
        if n == 0:
            print("j'ai gagné")
            break