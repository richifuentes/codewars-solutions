def diagonalDifference(arr):
    sum1 = int()
    sum2 = int()
    for i in range(len(arr)):
        sum1 = sum1 + arr[i][i]
    x = len(arr)-1
    for j in range(len(arr)):
        sum2 = sum2 + arr[j][x]
        x -= 1
    return abs(sum1-sum2)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
