def main():
    quote = str(input("Podaj zdanie:\n"))

    quote = quote.upper()
    wordList = quote.split()

    word_list(wordList)


def word_list(wordList):
    length = 0
    longest = 0

    for i in range(0, len(wordList)):
        checked = palindrome(wordList[i])
        if checked:
            checkLenght = len(wordList[i])
            if checkLenght >= length:
                length = checkLenght
                longest = i
        else:
            continue

    print(wordList[longest])



def palindrome(n):
    i = len(n)
    i = int(i)
    while i:
        i -= 1
        if n[i] != n[-i - 1]:
            return False
    return True


main()
