def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        for char in newpassword:
            if char.isdigit():
                return True
        return False
    else:
        return False
oldpassword = "wachtwoord"
newpassword = input("Wat wordt uw nieuwe wachtwoord?: ")
print(new_password(oldpassword,newpassword))