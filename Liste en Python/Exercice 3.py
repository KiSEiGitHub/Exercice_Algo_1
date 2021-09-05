def main():
    print('Entrer 5 nombres')
    t = [int(input(">> ")) for _ in range(5)]

    print(f"Liste: {t}")
    print(f"Max: {max(t)}")
    print(f"Min: {min(t)}")
    print(f"étendue: {max(t) - min(t)}")


if __name__ == '__main__':
    main()