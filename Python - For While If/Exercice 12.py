def main():
    p = 0.0001
    x = 1
    while x ** 2 < 2:
        x += p

    print(round(x -p , 4), round(x, 4))


if __name__ == '__main__':
    main()