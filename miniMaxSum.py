#!/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l1 = arr.copy() #  used to copy arr and pop one item then sum
    l2 = list() #  here I will store the sums
    for i in range(len(arr)):
        l1 = arr.copy()
        l1.pop(i)
        l2.append(sum(l1))
    print(str(min(l2)) + ' ' + str(max(l2)))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
