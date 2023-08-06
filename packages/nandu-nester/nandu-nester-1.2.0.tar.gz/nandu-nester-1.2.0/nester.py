def printme(l,indent=False,level=0):
    if isinstance(l,list):
        for l1 in l:
            printme(l1,indent,level+1)
    else:
        if indent:
            for i in range(level):
                print('\t',end='')

        print(l)


