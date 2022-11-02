def main():
    name = str(input("Podaj imie: "))
    name2 = str(input("Podaj imie: "))
    
    n = int(input("Podaj liczbe: "))

    suma = 0

    zadanie_pierwsze(name)
    zadanie_drugie(name2)

    zadanie_trzecie_for(n, suma)
    zadanie_trzecie_while(n, suma)
    zadanie_czwarte(n, suma)

def zadanie_pierwsze(name):
    print("Zadanie pierwsze:\n")

    print("Witaj "+ name)

def zadanie_drugie(name2):
    print("Zadanie drugie:\n")

    if name2 == "Anna" or name2 == "Jan":
        print("Witaj " + name2)
    else:
        print("Witaj")

def zadanie_trzecie_for(n, suma):
    for i in range(1, n+1):
        suma = suma + i
    
    print("Zadanie trzecie:")
    print(suma)

def zadanie_trzecie_while(n, suma):
    i = 1
    while i < n + 1:
        j = i

        suma = suma + j
        i = i + 1

    print(suma)

def zadanie_czwarte(n, suma):
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            suma = suma + i
        else:
            continue

    print(suma)

def zadanie_piate():
    pass

__name__ = main()