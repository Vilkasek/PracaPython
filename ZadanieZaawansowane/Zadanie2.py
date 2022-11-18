def palindrome(n):
    n = n.upper()

    i = len(n)
    i = int(i)
    while i:
        i -= 1
        if n[i] != n[-i-1]:
            return False
    return True

def main():
    word = str(input("Podaj słowo, które chcesz sprawdzić, czy jest palindromem: "))

    if palindrome(word):
        print("Tak to jest palindrom")
    else:
        print("To nie jest palindrom")

main()