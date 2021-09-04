while True:
    try:
        n = int(input("Nombre: "))
        p = int(input("Puissance: "))
        break
    except ValueError:
        print("Entrer un nombre")

for _ in range(p+1):
    print(n ** _)