def array_diff(a, b):
    if len(b) == 0:
        return a
    y = len(a)
    while (y > 0):
        for i in range(len(a)):
            for x in range(len(b)):            
                if a[i] == b[x]:
                    a.pop(i)
                    break
            else:
                continue
            break
        y = y - 1
    return a
