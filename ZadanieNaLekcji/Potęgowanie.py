number = int(input("Podaj swoją liczbę: "))
power = int(input("Podaj do której potęgi chcesz ją podnieść: "))

for i in range(0, power + 1):
    if i == 0:
        print("1")
    elif i == 1:
        number = number
        print(number)
    else:
        number *= number
        print(number)
