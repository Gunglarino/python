from datetime import datetime
import csv

surname = None
currentDate = datetime.today().strftime("%a %d %b %Y")
currentTime = datetime.today().strftime("%H:%M")
formattedDate = currentDate + ' at ' + currentTime

with open('login.csv', 'w', newline='') as file:
    fileWriter = csv.writer(file, delimiter=';',)

    while not surname == 'einde':
        surname = input('Voer uw achternaam in: ')

        if surname != 'einde':
            initials = input('Voer de voorletters van uw naam in: ')
            dateOfBirth = input('Voer uw geboortedatum in: ')
            emailAddress = input('Voer uw e-mailadres in: ')

            fileWriter.writerow([formattedDate] + [initials, surname, dateOfBirth, emailAddress])
