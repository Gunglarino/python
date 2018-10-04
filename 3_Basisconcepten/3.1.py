cijferICOR = 6
cijferPROG  = 7
cijferCSN = 8

totaal = sum([cijferICOR, cijferPROG , cijferCSN])
gemiddelde = totaal / 3
beloning = totaal * 30
overzicht = "Je gemiddelde is een: "+str(gemiddelde) + "\n" + "Als beloning voor je cijfers krijg je: €"+ str(beloning)
print(overzicht)