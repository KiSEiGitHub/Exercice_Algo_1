from random import randint

def main():

    nb_mystere = randint(1, 100)
    essaie = 4

    print("Nombre mystère entre 1 et 100")
    a = None
    while a != nb_mystere and essaie >= 1:
        a = int(input(">> "))

        if a == nb_mystere:
            print("Gagné")
        elif a < nb_mystere:
            print("c'est +")
            essaie -= 1
            if essaie <= 0:
                print("vous avez perdu")
        elif a > nb_mystere:
            print("C'est -")
            essaie -= 1
            if essaie <= 0:
                print("vous avez perdu")


if __name__ == '__main__':
    main()