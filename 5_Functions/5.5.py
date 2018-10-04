def kwadraten_som(grondgetallen):
    sum = 0
    for nummer in grondgetallen:
        if nummer > 0:
            sum = sum + nummer**2
    return sum
print(kwadraten_som([2,4,3,-1,10,-4]))