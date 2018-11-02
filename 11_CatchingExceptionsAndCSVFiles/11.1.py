persons = input('Hoeveel mensen gaan mee?')
try:
    4356 / int(persons)

    if 0 > int(persons):
        print('Aantal = ' + persons + ' - Negatieve getallen zijn niet toegestaan!')
    else:
        print('4356 / ' + persons + ' = ' + str(4356 / int(persons)))
except ZeroDivisionError:
    print('Aantal = ' + persons + ' - Delen door nul kan niet')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
else:
    print('Onjuiste invoer!')
