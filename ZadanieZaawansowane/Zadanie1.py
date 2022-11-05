def check(x, y):
    if x < 0 or y > 50000:
        print("Nie prawidłowy zakres, wpisz inny.")
        return False
    else:
        return True


def ideal(x, y):
    pass


def main():
    while True:
        a = int(input("Podaj początek ciągu, większy lub równy 0: "))
        b = int(input("Podaj koniec ciągu, ale mniejszy od 50000: "))

        if check(a, b):
            pass


main()
