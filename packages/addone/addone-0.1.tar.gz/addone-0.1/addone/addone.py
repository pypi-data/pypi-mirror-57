def addone(x):
    y = []
    for i in x:
        if isinstance (i,int) or  isinstance (i,float):
            y.append(i+1)
        else:
            y.append(i)
    return y