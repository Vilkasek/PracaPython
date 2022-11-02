# Aby rok przestępny był rokiem przestępnym musi być podzielny równocześnie przez 4, ale nie przez 100

rok = int(input("Podaj rok: "))
i = 0

def rokPrzestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True

    else:
        return False


while i < 20:
    if rokPrzestepny(rok):
        i += 1
        print(rok)
        rok += 4
    else:
        rok = rok + 1