def main():
    quote = str(input("Podaj zdanie:\n"))

    quote = quote.upper()
    wordList = quote.split()

    for i in range(0, len(wordList)):
        checked = palindrome(wordList[i])
        if checked:
            print(wordList[i])
        else:
            continue



def palindrome(n):
    i = len(n)
    i = int(i)
    while i:
        i -= 1
        if n[i] != n[-i - 1]:
            return False
    return True


main()
