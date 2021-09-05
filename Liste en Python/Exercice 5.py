from random import randint


def main():
    liste = ['Chien', 'Chat', 'Mouton', 'Vache']
    for item in liste:
        a = randint(0, len(liste) - 1)
        b = randint(0, len(liste) - 1)
        liste[a], liste[b] = liste[b], liste[a]
        print(liste)


if __name__ == '__main__':
    main()