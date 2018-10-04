import datetime
textFile = open("hardlopers.txt","a")
i=0
while True:
    runner = input("Naam van renner (Type klaar als u klaar bent): ")
    if runner == "klaar":
        break
    current = datetime.datetime.today()
    timeStamp = current.strftime("%a %d %b %Y, %X")
    textFile.write(timeStamp+", "+runner+"\n")
