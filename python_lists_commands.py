if __name__ == '__main__':
    N = int(input()) #  number of commands to run
    L = [] #  The list to perform commands on it.
    for i in range(0,N):
        b = list(input().split())
        if b[0] == 'insert':
            args = 'L.' + b[0] + '(' + b[1] + ', ' + b[2] + ')'
            try: eval(args)
            except: next
        elif len(b) == 2:
            args = 'L.' + b[0] + '(' + b[1] + ')'
            try: eval(args)
            except: next
        else:
            if b[0] == 'print':
                args = b[0] + '(L)'
                try: eval(args)
                except: next
            else:
                args = 'L.' + b[0] + '()'
                try: eval(args)
                except: next
