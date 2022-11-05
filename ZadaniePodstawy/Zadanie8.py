import random

proby = 0
test = 0

los = random.randint(0, 255)

win = False
while not win:
    traf = int(input("Podaj swój strzał: "))

    if traf == test:
        proby += 0
    else:
        proby += 1

    test = traf

    if los < traf:
        print("Za dużo")
    elif los > traf:
        print("Za mało")
    elif los == traf:
        print("Tyle razy strzelaliście:", proby)
        win = True
