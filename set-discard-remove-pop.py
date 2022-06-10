if __name__ == '__main__':
    n = int(input()) #number of elements on the set
    s = set(map(int, input().split())) #the set
    m = int(input()) #number of commands
    commands = []
    for i in range(0,m):
        command = input()
        b = list(command.split())
        if len(b) > 1:
            method = b[0]
            num = b[1]
            args = 's.' + method + '(' + num + ')'
            try:
                eval(args)
            except:
                next
        else:
            method = b[0]
            args = 's.' + method + '()'
            try:
                eval(args)
            except:
                next
    print(sum(s))
