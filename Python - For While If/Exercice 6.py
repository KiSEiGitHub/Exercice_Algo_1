from cmath import pi


def main():
    ez = 10
    for a in range(1, 100):
        for b in range(1, 100):
            if abs(pi - a / b ) < ez:
                ez = abs(pi - a / b)
                print(f"{a} / {b} {ez}")


if __name__ == '__main__':
    main()