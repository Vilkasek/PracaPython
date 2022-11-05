import decimal


def menu():
    choose = int(input("W jakim systemie podajesz liczbę?\n1. Dziesiętnym\n2. Szesznastkowym\n"))

    if choose == 1:
        dec_hex()
    elif choose == 2:
        hex_dec()


def dec_hex():
    n = int(input("Podaj całkowitą w dziesiętnym: "))
    hexagon = hex(n)
    print(hexagon.upper())


def hex_dec():
    s = str(input("Podaj liczbę całkowitą w szesnastkowym: "))
    n = int(s, base=16)
    print(n)

menu()