def divisible_by_7():
    result=[]
    for i in range(2000,3200,1):
        a = i % 7
        if (i%7==0) and (i%5!=0):
            result.append(i)
    return result
