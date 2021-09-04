while True:
    try:
        table = int(input("Table: "))
        break
    except ValueError:
        print("Vous devez entrer un nombre")

for i in range(1, 11):
    print(f"{table} * {i} = {table * i}")