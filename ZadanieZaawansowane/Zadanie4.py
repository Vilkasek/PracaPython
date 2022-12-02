quote = input("Podaj zdanie, długości do 64 znaków:\n")
length = len(quote)

table = []

def main():
    dimension = length ** (1 / 2)
    dimension = int(dimension)

    if length < 64:
        table_maker(table, dimension + 1)
        fill(table, quote, dimension)
        print(table)
    else:
        print("Podałeś za długie zdanie.")


def table_maker(t, d):
    for i in range(d):
        t.append([] * d)


def fill(t, q, d):
    pass


if __name__ == '__main__':
    main()
