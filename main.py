def main():
    name = str(input("Podaj imie: "))
    name2 = str(input("Podaj imie: "))
    
    n = int(input("Podaj liczbe: "))

    suma = 0

    zadanie_pierwsze(name)
    zadanie_drugie(name2)

    zadanie_trzecie_for(n, suma)
    zadanie_trzecie_while(n, suma)

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
    
    print("Zadanie trzecie:\n", suma)

def zadanie_trzecie_while(n, suma):
    i = 1
    while i < n + 1:
        # if i <= 0:
        #     j = i + 1
        # else:
        #     j = i

        j = i

        suma = suma + j
        i = i + 1

    print(suma)

__name__ = main()