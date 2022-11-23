def main():
    tab = [1, 5, 6, 2, 0, 3, 9]
    tab.sort()
    left = tab[0]
    right = len(tab) - 1

    looking = int(input("Podaj szukaną liczbę: "))

    n = binary_search(tab, left, right, looking)

    if n != None:
        print("Znaleziono", n)
    elif n == None:
        print("Nic nie znaleziono")

def binary_search(tab, left, right, x):
    if left <= right:
        mid = (left + right)/2
        mid = int(mid)
        if x < tab[mid]:
            return binary_search(tab, left, mid - 1, x)
        if x == tab[mid]:
            return mid
        return binary_search(tab, mid + 1, right, x)

main()