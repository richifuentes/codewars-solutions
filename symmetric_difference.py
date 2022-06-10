if __name__ == '__main__':
    Y = input()
    if len(Y)== 1:
        M = input()
    Z = input()
    if len(Y)== 1:
        N = input()
    listM = M.split()
    listN = N.split()
    a = set(map(int, listM))
    b = set(map(int, listN))
    results = a.symmetric_difference(b)
    x = sorted(results, key=int)
    for i in x:
        print(i)
