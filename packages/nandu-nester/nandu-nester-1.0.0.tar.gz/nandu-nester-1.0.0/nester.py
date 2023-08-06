def printme(l):
    if isinstance(l,list):
        for l1 in l:
            printme(l1)
    else:
        print(l)


