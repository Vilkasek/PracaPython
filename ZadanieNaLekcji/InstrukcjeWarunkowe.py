age = int(input("Podaj swój wiek: "))

def check(x):
    if x >= 18:
        return True
    else:
        return False

age = check(age)

match age:
    case True:
        print("Jesteś pełnoletni")
    case False:
        print("Jesteś dzieckiem")

number = int(input("Podaj liczbę: "))

if number > 0:
    print("Dodatnia")
else:
    print("Ujemna")

peron = int(input("Sprawdź gdzie jadą pociongi z danego peronu. Podaj peron: "))

match peron:
    case 1:
        print("Katowice")
    case 2:
        print("Gliwice")
    case 3:
        print("Częstochowa")
    case 4:
        print("Mysłowice")
    case 5:
        print("Kołobrzeg")
    case _:
        print("Nie ma takiego peronu")

def func_while(suma):
    n = int(input("Podaj liczbe: "))

    i = 1
    while i < n + 1:
        j = i

        suma = suma + j
        i = i + 1
    print(suma)

func_while(0)