def order(sentence):
    # code here
    word = sentence.split() # split the string in all the words
    
    # Create a dictionary with the pairs of position and word, not ordered.
    result = {}
    for x in range(len(word)):
        word0 = word[x]
        for y in range(len(word0)):
            char2 = word0[y]
            if char2.isdigit() == True:
                result.update({char2: word[x]})

    # Here will create the ordered list with position and words
    liste = []
    for z in range(len(word)):
        if z+1 > len(word):
            break
        indexDict = str(z + 1)
        liste.append(result.get(indexDict))

    # Finally will join the list into one single string and return the results.
    finalString = " ".join(liste)

    return finalString
