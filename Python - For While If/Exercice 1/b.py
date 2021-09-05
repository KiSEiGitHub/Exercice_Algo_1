def main():
    a = 0
    for i in range(1, 101):
        if i % 2 == 1:
            a += i

    print(a)

def plustechnique():
    a = sum(i for i in range(1, 101) if i % 2 == 1)
    print(a)

if __name__ == '__main__':
    main()