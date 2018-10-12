def code(invoerstring):
    lst = []
    for letter in invoerstring:
        lst.append(chr(ord(letter) + 3))
    encrypted = "".join(lst)
    return encrypted

naam = input("Naam: ")
begin = input("Beginstation: ")
eind = input("Eindstation: ")
print(code(naam+begin+eind))