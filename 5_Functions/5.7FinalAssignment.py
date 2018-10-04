def standaardtarief(afstand):
    if afstand > 50:
        prijs = 15 + afstand * 0.6
    elif afstand <=0:
        prijs = 0
    else:
        prijs = afstand * 0.8
    return prijs

def ritprijs(leeftijd, weekendRit, afstandKM):
    standaardPrijs = standaardtarief(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendRit:
            kosten = standaardPrijs*0.65
        else:
            kosten = standaardPrijs * 0.7
    else:
        if weekendRit:
            kosten = standaardPrijs * 0.6
        else:
            kosten = standaardPrijs
    return round(kosten,2)

leeftijd = int(input("Wat is uw leeftijd?: "))
weekendRit = bool(input("Is het in het weekend? (True/False):"))
afstandKM = int(input("Hoelang is de rit in KM?: "))
print("Uw rit kost: "+str(ritprijs(leeftijd, weekendRit, afstandKM))+" Euro")