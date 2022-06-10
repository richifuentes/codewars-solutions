if __name__ == '__main__':
    y = input() #number of students
    a = set(map(int, input().split())) #roll numbers English
    z = input() #number of students
    b = set(map(int, input().split())) #roll numbers French
    c = a.union(b)
    print(len(c))
