def openOrSenior(data):
    # Hmmm.. Where to start?
    result = []
    for i in range(len(data)):
        for x in range(0,1):
            if data[i][x] >= 55 and data[i][x+1] > 7:
                result.append('Senior')
            else:
                result.append('Open')

    return(result)                
