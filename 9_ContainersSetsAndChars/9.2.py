import random
def monopolyworp():

    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
        print(str(dice1) + " + " + str(dice2) + " = " + str(dice1 + dice2) + " (dubbel)")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2:
            print(str(dice1) + " + " + str(dice2) + " = " + str(dice1 + dice2) + " (dubbel)")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1 == dice2:
                print(str(dice1) + " + " + str(dice2) + " = (direct naar gevangenis)")
            else:
                print(str(dice1) + " + " + str(dice2) + " = " + str(dice1 + dice2))
        else:
            print(str(dice1) + " + " + str(dice2) + " = " + str(dice1 + dice2))
    else:
        print(str(dice1) + " + " + str(dice2) + " = " + str(dice1 + dice2))

while True:
    input("Druk op een knop om te rollen")
    monopolyworp()