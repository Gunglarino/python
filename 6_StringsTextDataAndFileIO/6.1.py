def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def table():
    print('  {:12}{:10}'.format("F", "C"))
    for celsius in range(-30,50,10):
        fahrenheit = convert(celsius)
        print("{:5} {:10}".format(fahrenheit,celsius))
table()
