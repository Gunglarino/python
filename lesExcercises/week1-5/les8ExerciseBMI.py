def BMI(height,weight):
    BMI = (weight * 703)/height**2
    if BMI > 25:
        print("You're to fat")
    elif BMI < 18.5:
        print("You're to skinny")
    else:
        print("You're good fam")

height = int(input("What is your height in inches? "))
weight = int(input("What is your weight in pounds? "))
BMI(height,weight)
