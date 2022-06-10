def anagrams(word, words):
    results = {} #This is a Set
    results2 = {} 
    results3 = []
    
    #Here it will count the apprearences with each char in word variable.
    for i in range(len(word)):
        chars = word
        try:
            out = word[i]
        except IndexError:
            break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] +=1
        results[chars] = char_dict

    #Here it will count the apprearences with each char in all words variables.
    for x in range(len(words)):
        chars2 = words[x]
        for y in range(len(chars2)):
            chars3 = words[x]
            try:
                out2 = chars2[y]
            except IndexError:
                break
            char_dict2 = results2.get(chars2, {})
            char_dict2.setdefault(out2, 0)
            char_dict2[out2] +=1
            results2[chars2] = char_dict2

    for z in range(len(words)):
        chars3 = words[z]
        if results[word] == results2[chars3]:
            results3.insert(z, chars3)
            
    return results3
