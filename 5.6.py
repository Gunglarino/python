def wijzig(letterLijst):
    del letterLijst[:]
    letterLijst.append("d")
    letterLijst.append("e")
    letterLijst.append("f")
letterLijst = ["a", "b", "c"]
print(letterLijst)
wijzig(letterLijst)
print(letterLijst)
#
# # 1. Doordat de strings in de lst inmutable zijn
# # 2. Nee want ik gebruik lijst functies
# # 3. Dat je de items niet direct kan veranderen als die inmutable zijn