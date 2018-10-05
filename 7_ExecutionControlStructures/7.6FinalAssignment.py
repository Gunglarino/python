# check if locker exist if not create it
try:
    fh = open('locker.txt', 'r')
    print("EXIST")
except FileNotFoundError:
    print("doesnt exist")
    firstInit = open('locker.txt', 'w')
    firstInit.close()

# Checks if there are free lockers and returns a list of free lockers
def listFreeLockers():
    lockerFile = open('locker.txt', 'r+')
    lst = lockerFile.readlines()
    lockerList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", ]
    usedList = []
    # Loops to lockers and get locker number
    for locker in lst:
        lockerSplitNumbers = locker.split(",")
        usedList.append(lockerSplitNumbers[0])

    # If locker exist it isn't free
    for i in usedList:
        if i in lockerList:
            lockerList.remove(i)

    lockerFile.close()
    return lockerList

# OPTION 1 prints out free lockers
def checkFree():
    lockerList = listFreeLockers()
    string = ', '.join(lockerList)
    if len(lockerList) == 0:
        input("Helaas, alle kluizen zijn al in gebruik (Druk op enter om terug te gaan): \n")
        menu()
    else:
        print("De vrije kluizen zijn: "+string)
        input("Druk op enter om terug te gaan: \n")
        menu()

# OPTION 2 gives user a locker with password
def newLocker():
    lockerFile = open('locker.txt', 'a')
    lockerList = listFreeLockers()

    if len(lockerList) == 0:
        input("Helaas, alle kluizen zijn al in gebruik (Druk op enter om terug te gaan): \n")
        menu()

    print("U krijgt kluis: "+lockerList[0])
    wachtwoord = input("Type een wachtwoord van minimaal 4 characters: ")

    while len(wachtwoord) < 4:
        print("Wachtwoord te kort probeer het nog eens: ")
        wachtwoord = input("Type een wachtwoord van minimaal 4 characters: ")

    while "," in wachtwoord:
        print("Wachtwoord mag helaas geen comma bevatten: ")
        wachtwoord = input("Type een wachtwoord van minimaal 4 characters: ")

    lockerFile.write(lockerList[0]+","+wachtwoord+"\n")
    lockerFile.close()
    input("Wachtwoord is toegevoegd aan kluis: "+lockerList[0]+" (druk op enter om terug te gaan)\n")
    menu()

# OPTION 3 opens the locker for the user
def openLocker():
    lockerFile = open('locker.txt', 'r+')
    kluisnummer = input("wat is uw kluisnummer: ")
    wachtwoord = input("wat is uw wachtwoord: ")
    line = kluisnummer+","+wachtwoord+"\n"
    lst = lockerFile.readlines()
    if line in lst:
        input("Uw heeft toegang tot uw kluis (Druk op enter om terug te gaan): \n")
        menu()
    else:
        print("Uw kluisnummer of wachtwoord is incorrect")
        fouteInput = input("Type 1 om het nog een keer te proberen of 2 om terug te gaan: ")
        if fouteInput == "1":
            openLocker()
        elif fouteInput == "2":
            menu()

    lockerFile.close()

# OPTION 4 free the locket from user
def deleteLocker():
    lockerFile = open('locker.txt', 'r+')
    kluisnummer = input("wat is uw kluisnummer: ")
    wachtwoord = input("wat is uw wachtwoord: ")
    line = kluisnummer + "," + wachtwoord + "\n"
    lst = lockerFile.readlines()
    lockerFile.close()
    lockerFile = open('locker.txt', 'r+')
    for i in lst:
        if i != line:
            lockerFile.write(i)

    lockerFile.truncate()
    lockerFile.close()
    lockerFile.close()
    input("Uw kluis is vrijgegeven aan andere gebruikers (Druk op enter om terug te gaan): ")
    menu()

# Main menu Text
def menu():
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug")
    menuOptie = input("Type het nummer van de actie die u wilt doen?: ")
    cycle(menuOptie)

# Option selector
def cycle(menuOptie):
    if menuOptie == "1":
        checkFree()
    elif menuOptie == "2":
        newLocker()
    elif menuOptie == "3":
        openLocker()
    elif menuOptie == "4":
        deleteLocker()
    else:
        print("ongeldige invoer, probeer 1,2,3,4 als invoer: ")
        menu()

menu()

