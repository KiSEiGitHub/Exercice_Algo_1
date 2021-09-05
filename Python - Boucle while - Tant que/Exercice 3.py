def main():
    etage = 0
    bille = 0

    while bille <= 1000:
        etage += 1
        bille += etage**2
    print(f"Elle pourra avoir {etage} étages")

if __name__ == '__main__':
    main()