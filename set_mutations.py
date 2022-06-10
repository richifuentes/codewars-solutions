if __name__ == '__main__':
    y = input() #number of elements in set
    A = set(map(int, input().split())) #set A
    n = int(input()) #number of other sets
    for i in range(0,n):
        b = list(input().split())
        method = b[0]
        B = set(map(int, input().split())) #set B
        args = 'A.' + method + '(' + 'B' + ')'
        eval(args)
    print(sum(A))
