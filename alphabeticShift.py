word = input()
myList = list(word)

alpha = list('abcdefghijklmnopqrstuvwxyz')
result = str()
for i in range(len(myList)):
    x = alpha.index(myList[i])
    if x == 25:
        result = result + alpha[0]
    else:
        result = result + alpha[x+1]
print(result)
