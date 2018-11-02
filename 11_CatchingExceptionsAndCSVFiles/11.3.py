import csv

lines = []

with open("gamers.csv", "r", newline="") as file:
    fileReader = csv.reader(file, delimiter=";")

    [lines.append("; ".join(row)) for row in fileReader]
    highestStringList = max(lines[-2:]).split(";")

    name = highestStringList[0]
    date = highestStringList[1].replace(" ", "")
    score = highestStringList[2].replace(" ", "")

    print("De hoogste score is: " + score + " op " + date + " behaald door " + name)