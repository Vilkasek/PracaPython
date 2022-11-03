k = float(input("Podaj k: "))
n = int(input("Podaj zakres ciągu: "))

summary = 0
power = 0

def sumar(summary):
    numer = 0

    for i in range(0, n):
        numer = num(i)

        summary = summary + numer
    
    summary = summary * 4
    print(summary)

def num(i):
    minusOne = (-1)
    divider = 2 * (k + i) - 1
    power = (k + i) + 1
    
    return float(minusOne ** power / divider)

sumar(summary)
