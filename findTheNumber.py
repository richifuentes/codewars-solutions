#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findNumber function below.
def findNumber(arr, k):
    try:
        index = arr.index(k)
        if isinstance(index,int) == True:
            return "YES"
    except:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()
