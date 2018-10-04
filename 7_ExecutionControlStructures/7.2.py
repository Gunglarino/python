inputLst = eval(input("Geef lijst met minimaal 10 strings: "))
newLst = []
for woord in inputLst:
    if len(woord) == 4:
        newLst.append(woord)

print("De nieuw-gemaakte lijst met alle vier-letter strings is: "+str(newLst))
