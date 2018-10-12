def inlezen_beginstation(stations):
    station = input("Wat is je beginstation: ")

    # keep asking for station if station is not in traject
    while station not in stations:
        print("Station niet gevonden in traject probeer opnieuw")
        station = input("Wat is je beginstation: ")
    return station

def inlezen_eindstation(stations, beginstation):
    station = input("Wat is je eindstation: ")

    # keep asking for station if station is not in traject
    while station not in stations:
        print("Station niet gevonden in traject probeer opnieuw")
        station = input("Wat is je eindstation: ")

    # check of eindstation na beginstation komt
    if stations.index(station) > stations.index(beginstation):
        return station
    else:
        print("Station is het zelfde of is eerder in het traject dan het beginstation probeer opnieuw")
        inlezen_eindstation(stations, beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    beginIndex = stations.index(beginstation)
    eindIndex = stations.index(eindstation)
    afstand = eindIndex-beginIndex

    # Tussenstoppen maken met gegeven begin en eind station
    lst = []
    for tussenstop in range(beginIndex+1,eindIndex):
        lst.append(stations[tussenstop]+ " - ")
    tussenstoppen = "".join(lst)

    print("Het beginstation "+beginstation+ " is het "+ str(beginIndex+1)+"e station in het traject.")
    print("Het eindstation " + eindstation + " is het " + str(eindIndex + 1) + "e station in het traject.")
    print("De afstand bedraagt "+ str(afstand)+" station(s).")
    print("De prijs van het kaartje is "+str(afstand * 5)+" euro.\n")
    print("Je stapt in de trein in: "+ beginstation)
    print(tussenstoppen)
    print("Je stapt uit in: "+ eindstation)

stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", " ’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
