def printme(l,v=0):
    if isinstance(l,list):
        for l1 in l:
            printme(l1,v+1)
    else:
        for i in range(v):
            print('\t',end='')
        print(l)


