while True:
    try:
        n = int(input("n: "))
        break
    except ValueError:
        print("vous devez rentrer un nombre")

if n % 2 == 0:
    print(f"{n} est pair")
else:
    print(f"{n} n'est pas pair")