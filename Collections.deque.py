from collections import deque
n = int(input()) #number of commands
d = deque()
for i in range(n):
    cmd = input().split()
    #b = list(command.split())
    if len(cmd) > 1:
        method = cmd[0]
        num = cmd[1]
        args = "d." + method + '(' + num + ')'
        try:
            eval(args)
        except:
            next
    else:
        method = cmd[0]
        args = 'd.' + method + '()'
        try:
            eval(args)
        except:
            next
for x in d:
    print(x, end=' ')
