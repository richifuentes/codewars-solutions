def create_phone_number(n):
    #your code here
    result = "("
    for i in range(len(n)):
        if i < 3:
            result = result + str(n[i])
            if i == 2:
                result = result + ")"
        elif i == 3:
            result = result + " " + str(n[i])
        elif i > 3 and i < 6:
            if i == 5:
                result = result + str(n[i]) + "-"
            else:
                result = result + str(n[i])
        elif i >= 6 and i <=9:
                result = result + str(n[i])
        
    return result
