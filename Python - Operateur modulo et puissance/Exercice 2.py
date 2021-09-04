while True:
    try:
        n = int(input('n: '))
        break
    except ValueError:
        print('n dois êtes un nombre')

for i in range(1, n + 1):
    if n % i == 0:
        print(i)