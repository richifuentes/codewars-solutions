if __name__ == '__main__':
    y = input() #number of students
    a = set(map(int, input().split())) #roll numbers English
    z = input() #number of students
    b = set(map(int, input().split())) #roll numbers French
    c = a.intersection(b)
    print(len(c))
