o = 0
while True:
    try:
        e = int(input("Nombre d'étages: "))
        break
    except ValueError:
        print("Vous devez rentrer un nombre")
for i in range(1, e+1):
    o = o + i

print(f"Il lui faudra {o} billes pour une pyramide de {e} étages")