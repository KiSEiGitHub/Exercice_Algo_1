def natureorno(x):
    c = sum(x % i == 0 for i in range(1, x+1))
    if c == 2:
        print(f"{x} est premier")
    else:
        print(f"{x} n'est pas premier")


natureorno(2)