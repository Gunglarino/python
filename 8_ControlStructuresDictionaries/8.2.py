while True:
    word = input("Geef een string van vier letters: ")
    if len(word) == 4:
        break
    print(word+" heeft "+str(len(word))+" letters")
print(word+" is een correcte string van 4 characters")