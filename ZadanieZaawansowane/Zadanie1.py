def check(x, y):
    if x < 0 or y > 50000:
        print("Nie prawidłowy zakres, wpisz inny.")
        return False
    else:
        return True


def divides(n):
    d = []
    for i in range(1, int((n/2) + 1)):
        if n % i == 0:
            d.append(i)
    return d


def ideal(n):
    suma = 0
    for i in divides(n):
        suma += i

    if suma == n:
        print(n, "to liczba doskonała.")


def main():
    while True:
        a = int(input("Podaj początek ciągu, większy lub równy 0: "))
        b = int(input("Podaj koniec ciągu, ale mniejszy od 50000: "))

        if check(a, b):
            for i in range(a, b + 1):
                ideal(i)


main()
