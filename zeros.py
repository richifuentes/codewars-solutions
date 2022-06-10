def zeros(n):
    z = 0
    if n==0:
        return 0
    y = 1
    for i in range(1, n+1):
       y = y*i
    x = str(y)
    for i in range(len(x)-1, 0, -1):
        if x[i]=='0':
            z += 1
        elif x[i] != 0:
            break
    return z
