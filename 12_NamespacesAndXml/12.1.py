import xmltodict

with open("artikelen.xml", "r") as f:
    xmldict = xmltodict.parse(f.read())

    for artikel in xmldict["artikelen"]["artikel"]:
        print(artikel["naam"])