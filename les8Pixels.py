def pixels(lst):
    accumalotor = 0
    for innerList in lst:
        for i in range(0,len(innerList)):
            if innerList[i] > 0:
                accumalotor = accumalotor + 1
                # print(innerList[i])
    return accumalotor
lst = [[0,40,23,0,4],[4,5,6,3,0],[0,0,0,1,0],[9,4]]
accu = pixels(lst)
print(accu)