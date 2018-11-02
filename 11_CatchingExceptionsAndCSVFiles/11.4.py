import csv

# READ
products = [[121, 'ABC123', 'Highlight pen', 231, 0.56],
            [123, 'PQR678', 'Nietmachine', 587, 9.99],
            [128, 'ZYX163', 'Bureaulamp', 34, 19.95],
            [137, 'MLK709', 'Monitorstandaard', 66, 32.50],
            [271, 'TRS665', 'Ipad hoes', 155, 19.01]]

with open('artikelen.csv', 'w+', newline='') as csv_file:
    csvWriter = csv.writer(csv_file, delimiter=",")
    csvWriter.writerow(["Artikelnummer", "Artikelcode", "Naam", "Voorraad", "Prijs"])
    for product in products:
        csvWriter.writerow(product)

# WRITE
lines = []
with open("artikelen.csv", "r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    [lines.append(line) for line in csvReader]

    lowestCount = 'unset'
    highestPrice = 0
    totalProducts = 0
    mostExpensiveProduct = []

    for line in lines[1:]:
        count = int(line[3])

        if lowestCount == 'unset':
            lowestCount = count
            lowestCountProduct = line
        elif lowestCount > count:
            lowestCount = count
            lowestCountProduct = line

        if float(line[4]) > highestPrice:
            highestPrice = float(line[4])
            mostExpensiveProduct = line
        totalProducts += int(line[3])

    print('Het duurste artikel is', mostExpensiveProduct[2], 'en die kost', mostExpensiveProduct[4])
    print("Er zijn slechts", lowestCountProduct[3], "exemplaren in voorraad van het product met nummer", lowestCountProduct[0])
    print('In totaal hebben wij', totalProducts, 'producten in ons magazijn liggen')