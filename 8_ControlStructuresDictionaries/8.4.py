def ticker(filename):
    dict = {}
    infile = open(filename, "r+")
    lst = infile.readlines()
    for item in lst:
        item = item[:-2]
        seperate = item.split(":")
        dict.update({seperate[0]:seperate[1]})
    return dict

beursDict = ticker("beurs.txt")
print("1. You have a company name: ")
print("2. You have a ticker symbol: ")
functionType = input("Type number of you action: ")

if functionType == "1":
    companyName = input("Enter company name: ")
    if companyName in beursDict:
        print("Ticker symbol: "+beursDict[companyName])
    else:
        print("Not a correct company name")

if functionType == "2":
    tickerSymbol = input("Enter ticker symbol: ")
    for name, symbol in beursDict.items():
        if symbol == tickerSymbol:
            print("company name: " + name)
