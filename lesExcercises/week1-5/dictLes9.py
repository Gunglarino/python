def wordtCount(text):
    dicto = {}
    lst = text.split()
    lst.sort()
    for word in lst:
        if word in dicto:
            dicto[word]= dicto[word] + 1
        else:
            dicto[word] = 1
    for word in dicto:
        if dicto[word] == 1:
            verb = " time"
        else:
            verb = " times"

        print(word," appears "+ str(dicto[word]) + verb)

text = "all animals are equal but some animals are more equal than other"
wordtCount(text)
