name = input('Enter your name: ')
age = int(input('Enter your age: '))
if age >= 18:
    eligible = "able"
else:
    eligible = "not able"
line = name + ', you are ' + eligible + ' to vote!'
print(line)
