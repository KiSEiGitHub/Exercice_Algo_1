def main():
    print("Entrer 5 nombre")
    t = [int(input(">> ")) for _ in range(5)]
    total = sum(t)
    print(f"Moyenne de la liste {total / 5}")



if __name__ == '__main__':
    main()