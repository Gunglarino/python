infile = open('kaartnummers.txt', 'r+')
lst = infile.readlines()
hoogsteGetal = 0

for regel in lst:
    regelSplit = regel.split(",")
    if hoogsteGetal < int(regelSplit[0]):
        hoogsteGetal = int(regelSplit[0])
        maxregelnummer = lst.index(regel) + 1
totalRegel = len(lst)
print("Deze file telt " + str(totalRegel) + " regels")
print("Het grootste kaartnummer is: "+str(hoogsteGetal)+" en dat staat op regel "+ str(maxregelnummer))
infile.close()