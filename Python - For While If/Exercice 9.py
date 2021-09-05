from dataclasses import dataclass
from random import randint


@dataclass
class Eleve:
    nom: str


eleve1 = Eleve('Tom')
eleve2 = Eleve('Marc')
eleve3 = Eleve('Lola')
eleve4 = Eleve('Jules')
eleve5 = Eleve('Thémis')
eleve6 = Eleve('Dorian')
eleve7 = Eleve('Laura')
eleve8 = Eleve('Kevin')
eleve9 = Eleve('Popo')
eleve10 = Eleve('Mouk')

classe = {
    1: eleve1.nom,
    2: eleve2.nom,
    3: eleve3.nom,
    4: eleve4.nom,
    5: eleve5.nom,
    6: eleve6.nom,
    7: eleve7.nom,
    8: eleve8.nom,
    9: eleve9.nom,
    10: eleve10.nom
}


def delegue(x, y):
    print(f"{x}: délégué 1")
    print(f"{y}: délégué 2")


def adjoint(x, y):
    print(f"{x}: adjoint 1")
    print(f"{y}: adjoint 2")


def main():

    while True:
        de = randint(1, 10)
        de2 = randint(1, 10)
        ae = randint(1, 10)
        ae2 = randint(1, 10)

        if de != de2 and ae != ae2 and de != ae and de2 != ae2 and de != ae2 and de2 != ae:
            delegue(classe.get(de), classe.get(de2))
            adjoint(classe.get(ae), classe.get(ae2))
            break
            

if __name__ == '__main__':
    main()