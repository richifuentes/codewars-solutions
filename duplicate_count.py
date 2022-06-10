def duplicate_count(text):
    results = dict()
    string = text.upper()
    for i in range(len(string)):
        x = string.count(string[i])
        if x > 1 :
            results.update({string[i]:x})
    return(len(results))
