import random


def main():

    tab = []

    fill(tab)

    print(tab)

    n = input("Czego szukasz w tej intowej tablicy?\nPodaj liczbę: ")


    search(n, tab)
    sorting(tab)


def fill(tab):
    for i in range(10):
        number = random.randint(0, 100)

        tab.append(number)


def search(n, tab):
    found = False
    # i = int(i)
    for i in range(0, len(tab)):
        if n == tab[i] and found == False:
            print("Jestem")
            found = True
        elif i + 1 >= len(tab) and found == False:
            print("Nie ma")


def sorting(tab):
    tab.sort()
    print(tab)


if __name__ == '__main__':
    main()
