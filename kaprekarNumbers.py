def kaprekarNumbers(p, q):
    r = list()
    for i in range(1,q):
        a = i ** 2
        b = str(a)
        if int(b[0]) + int(b[1]) == a:
            r.append(i)
    for j in range(len(r)):
        print([j],end=' ')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
