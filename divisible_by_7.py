def divisible_by_7():
    result=[]
    for i in range(2000,3200,1):
        a = i % 7
        if a == 0:
            b = i / 7
            c = b % 5
            if c == 0:
                result.append(i)
    return result
            
