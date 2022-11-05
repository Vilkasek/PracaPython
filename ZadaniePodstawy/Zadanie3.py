def func_for(suma):

    n = int(input("Podaj liczbe: "))

    for i in range(1, n + 1):
        suma = suma + i

    print(suma)


def func_while(suma):
    n = int(input("Podaj liczbe: "))

    i = 1
    while i < n + 1:
        j = i

        suma = suma + j
        i = i + 1
    print(suma)


func_for(0)
func_while(0)
