def gemiddelde():
    zin = input("Geef een zin op: ")
    letters = 0
    lst = zin.split(" ")
    for woord in lst:
        lengteWoord = len(woord)
        letters += lengteWoord
    print(round(letters/len(lst),2))
gemiddelde()