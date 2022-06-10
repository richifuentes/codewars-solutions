def hammingDistance(string1, string2):
    result = int()
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            result += 1
    return result
