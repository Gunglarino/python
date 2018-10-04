def som(getallenLijst):
    sum = 0
    for getal in getallenLijst:
        sum = sum + getal
    return sum
getallenLijst = [7,12,6,8,5,3,5,23,5,32]
print(som(getallenLijst))