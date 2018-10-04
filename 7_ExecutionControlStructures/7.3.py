invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lst = invoer.split("-")
i = 0
maxNumber = 0
minNumber = 999999999
while i < len(lst):
    lst[i] = int(lst[i])
    if maxNumber < lst[i]:
        maxNumber = lst[i]
    if minNumber > lst[i]:
        minNumber = lst[i]
    i += 1
lst.sort()
avarage = sum(lst)/len(lst)
print("Gesorteerde list van ints: " + str(lst))
print("Grootste getal: "+ str(maxNumber) +" en Kleinste getal: "+str(minNumber))
print("Aantal getallen: "+str(len(lst))+" en Som van de getallen: "+str(sum(lst)))
print("Gemiddelde: "+str(avarage))