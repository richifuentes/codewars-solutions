def oddNumbers(l, r):
    arr=[]
    for i in range(l,r+1,1):
        if i % 2 != 0:
            arr.append(i)
    return arr
