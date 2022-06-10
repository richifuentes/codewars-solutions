if __name__ == '__main__':
    K = int(input()) #Integer, the size of each Group
    A = list(map(int, input().split())) #the unordered elements of the room number list.
    if 1 < K < 1000:
        x = int(len(A) / K)  # get the number of groups
        for i in A:
            if i > x + 1:
                print(i)
                break
