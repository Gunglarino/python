leeftijd = int(input("Wat is uw leeftijd: "))
paspoort = input("Bent u in bezit van een Nederlands [paspoort (ja/nee): ").lower()
if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")