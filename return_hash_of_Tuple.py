if __name__ == '__main__':
    n = int(input())
    l = tuple(map(int, input().split()))
    print(hash(l))
