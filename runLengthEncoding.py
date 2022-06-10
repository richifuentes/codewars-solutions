def runLengthEncoding(inputString):
    count = int()
    result = str()
    myDict = dict()
    for i in range(len(inputString)):
        if inputString[i] == inputString[i+1]:
            myDict[inputString[i]] = 2
        else:
            if 
            myDict[inputString[i]] = 1
        






        if i == len(inputString)-1:
            result = result + "1" + inputString[i]
            break
        
            count += 1
            next
        else:
            if count > 1:
                result = result + str(count) + inputString[i]
            else:
                result = result + "1" + inputString[i]
    return result
