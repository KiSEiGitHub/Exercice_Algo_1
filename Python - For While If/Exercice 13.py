def main():
    a = 1
    b = 2

    while b - a > 0.001:
        m = (a + b) / 2
        if m ** 2 < 2:
            a = m
        else:
            b = m

    print(a, b)


if __name__ == '__main__':
    main()