infile = open('kaartnummers.txt', 'r+')
lst = infile.readlines()
for regel in lst:
    regelSplit = regel.split(",")
    regelSplit[1] = regelSplit[1].rstrip()
    print(regelSplit[1]+ "heeft kaartnummer: "+ regelSplit[0])
infile.close()