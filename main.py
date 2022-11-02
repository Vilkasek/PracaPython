def main():
    name = str(input("Podaj imie: "))
    name2 = str(input("Podaj imie: "))

    suma = 0
    iloczyn = 1

    zadanie_pierwsze(name)
    zadanie_drugie(name2)

    zadanie_trzecie_for(suma)
    zadanie_trzecie_while(suma)
    zadanie_czwarte(suma)
    zadanie_piate(suma, iloczyn)

def zadanie_pierwsze(name):
    print("Zadanie pierwsze:\n")

    print("Witaj "+ name)

def zadanie_drugie(name2):
    print("Zadanie drugie:\n")

    if name2 == "Anna" or name2 == "Jan":
        print("Witaj " + name2)
    else:
        print("Witaj")

def zadanie_trzecie_for(suma):
    n = int(input("Podaj liczbe: "))

    for i in range(1, n+1):
        suma = suma + i
    
    print("Zadanie trzecie:")
    print(suma)

def zadanie_trzecie_while(suma):
    n = int(input("Podaj liczbe: "))

    i = 1
    while i < n + 1:
        j = i

        suma = suma + j
        i = i + 1

    print(suma)

def zadanie_czwarte(suma):
    n = int(input("Podaj liczbe: "))

    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            suma = suma + i
        else:
            continue

    print(suma)

def zadanie_piate(suma, iloczyn):
    choose = int(input("1. Licz sumę \n2. Licz iloczy \nWybierz opcje: "))

    # Szybkie wyjaśnienie, dlaczego użyłem if i elif
    # Jest to spowodowane tak samo jak brak pętli do...while brakiem takowej funkcji
    # Fakt faktem mogłem zaimportować zewnętrzną bibliotekę, która zezwalała mi na użycie tej funkcji
    # Dlaczego więc tego nie zrobiłem?
    # Pomijając nieczytelną dokumentację, chciałem jednak ograniczyć się do czystego Pythona

    if choose == 1:
        zadanie_trzecie_while(suma)
    elif choose == 2:
        n = int(input("Podaj liczbe: "))
        for i in range(1, n+1):
            iloczyn = iloczyn * i
        print(iloczyn)


__name__ = main()