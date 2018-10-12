number = 1
count = 0
total = 0
while number != 0:
    number = int(input("Geef een getal: "))
    count  += 1
    total = total + number
print("Er zijn "+str(count)+" getallen ingevoerd, de som is: "+ str(total))