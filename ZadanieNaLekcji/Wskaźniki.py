quote = str(input("Podaj dane: \n"))

quote = quote.upper()
quote = quote.split(",")

for i in range(len(quote)):
    print(quote[i])