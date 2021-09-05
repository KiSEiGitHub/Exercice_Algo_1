from random import randint

point = 0
for _ in range(11):
    a = randint(1, 10)
    b = randint(1, 10)
    print(f"{a} * {b} ?")
    while True:
        try:
            c = int(input(">> "))
            break
        except ValueError:
            print("Vous devez rentrer un nombre")

    if c == a * b:
        print("+1 point")
        point += 1
    else:
        print("-1 point")
        point -= 1


print(f"Total point: {point}")