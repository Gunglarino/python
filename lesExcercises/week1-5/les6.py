# def hello(name):
#     print("wauw "+ name + " wat een slechte naam heb jij")
# hello("victor")
#
# def rng(lst):
#     minumum = min(lst)
#     maximum = max(lst)
#     range = maximum - minumum
#
#     return(range)
# between = rng([4,0,10,-5])

def swapFS(lst):
    if len(lst) >= 2:
        lst[0],lst[1] = lst[1],lst[0]
swapFS(["test","Next"])
