def fraction(x, y):
    i = 2
    while i <= x and i <= y:
        if x % i == 0 and y % i == 0:
            x = x // i
            y = y // i
        else:
            i += 1
    return x, y

while True:
    try:
        a = int(input("n: "))
        b = int(input("n: "))
        break
    except ValueError:
        print('n doit être un nombre')

t, o = fraction(a, b)
print(f"{t} / {o}")