def sum():
    total = 0
    while True:
        nextInt = input("next Int: ")
        if nextInt == "quit":
            break
        total = total + int(nextInt)
    return total

print(sum())