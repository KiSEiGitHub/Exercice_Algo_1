while True:
    try:
        n = int(input("n: "))
        break
    except ValueError:
        print("Vous devez rentrer un nombre")

if 6 % n == 0:
    print(f"{n} est divisible 6")
else:
    print(f"{n} n'est pas divisible par 6")