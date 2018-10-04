s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = ('aeiou')
for char in s:
    if char.lower() in klinker:
        print(char)