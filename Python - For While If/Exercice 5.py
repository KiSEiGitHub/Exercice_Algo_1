def main():
    for y in range(0, 11):
        for z in range(11):
            if y + z <= 10 and 2 * y + 5 * z == 30:
                print(10-y -z, y, z)


if __name__ == '__main__':
    main()