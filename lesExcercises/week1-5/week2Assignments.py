# We gaan een lijst bijhouden met je favoriete artiesten. We gaan de lijst eerst creëren met 1 artiest en dan uitbreiden.
# Schrijf per stap een expressie om:
#
# een nieuwe list met 1 artiest aan te maken met de naam favorieten.
# de lijst uit te breiden met een tweede artiest.
# de tweede artiest te vervangen door een andere naam.

# favorieten = ['Rapper Sjors']
# favorieten.append("Kendrick Lamar")
# favorieten[1] = "Beyonce"
# print(favorieten)



# Het bereik van een lijst is het verschil tussen het grootste en het kleinste getal.
#
# Schrijf een Python expressie die het bereik van een lijst berekent.
#
# Als bijvoorbeeld variabele list bestaat uit de getallen 3, 7, -2 en 12,
# dan moet de expressie evalueren naar 14 (verschil tussen 12 en -2).
# Zorg dat de expressie altijd werkt,
# ook al bestaat de lijst uit andere waarden!

# numbers = [1,7,3,76,13,57,3,34,45,7,400,-21,34]
# print(abs(min(numbers)) + abs(max(numbers)))



# De tuple letters kan in willekeurige volgorde de letters A, B en C bevatten. Bijvoorbeeld:
#
# letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
# Maak een nieuw bestand, bijvoorbeeld pe2_1.py,
# en schrijf een programma dat een nieuwe lijst maakt (en print) met het aantal voorkomens van de letters in alfabetische volgorde.
# Tuple letters bevat 2 keer ‘A’, 3 keer ‘B’ en 4 keer ‘C’.
# De lijst die dit programma maakt (en print) is dan: [2, 3, 4].
# from collections import Counter


# letters = ('a','f','b','a','f','c','d','c','e','a','e',)
# print(list(Counter(sorted(letters)).values()))
# print(list(Counter(sorted(letters)).values()))

tupleShadow = ['A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B', 'D']
sortedValues = []
[sortedValues.append(value) for key,
    value in sorted([[x, tupleShadow.count(x)]
    for x in set(tupleShadow)])]
print(sortedValues)