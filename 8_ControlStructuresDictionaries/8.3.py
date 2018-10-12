cijfers = {'Thomas': 9, 'Jasper': 6, 'Martijn': 7, 'Koen': 3, 'Jelle': 6, 'Bouke': 8, 'Tom': 10, 'Ryan': 5}
for naam in cijfers:
    cijfer = cijfers[naam]
    if cijfer >= 8:
        print(naam+" heeft een mooi cijfer namelijk: "+ str(cijfer))
