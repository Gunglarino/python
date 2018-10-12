def namen():
    dicto = {}
    naam = input("Volgende naam: ")

    while len(naam) != 0:
        if naam in dicto:
            dicto[naam]= dicto[naam] + 1

        else:
            dicto[naam] = 1
        naam = input("Volgende naam: ")

    for naam in dicto:
        if dicto[naam] == 1:
            zin = "Er is "
            student = " student met de naam "
        else:
            zin = "Er zijn "
            student = " studenten met de naam "

        print(zin + str(dicto[naam]) + student+naam)
namen()