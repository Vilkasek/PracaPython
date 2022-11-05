import math

n = int(input("Podaj zakres: "))

def pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(1, n+1):
    if pierwsza(i):
        print(i)