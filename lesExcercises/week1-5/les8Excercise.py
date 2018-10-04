def acronym():
    string = input("Waar wilt u een afkorting voor?")
    lst = string.split()
    afkorting = ''
    print(afkorting)
    for i in lst:
        afkorting = afkorting + i[0].upper()
    print(afkorting)
acronym()
