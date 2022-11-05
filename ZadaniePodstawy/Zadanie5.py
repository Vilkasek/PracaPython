from Zadanie3 import func_for

iloczyn = 0
choose = int(input("1. Licz sumę \n2. Licz iloczy \nWybierz opcje: "))
# Szybkie wyjaśnienie, dlaczego użyłem if i elif
# Jest to spowodowane tak samo jak brak pętli do...while brakiem takowej funkcji
# Fakt faktem mogłem zaimportować zewnętrzną bibliotekę, która zezwalała mi na użycie tej funkcji
# Dlaczego więc tego nie zrobiłem?

# Pomijając nieczytelną dokumentację, chciałem jednak ograniczyć się do czystego Pythona

if choose == 1:
    func_for()
elif choose == 2:
    n = int(input("Podaj liczbe: "))
    for i in range(1, n+1):
        iloczyn = iloczyn * i
print(iloczyn)