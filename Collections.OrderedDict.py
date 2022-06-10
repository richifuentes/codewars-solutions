from collections import OrderedDict
N = int(input())
order_dict = OrderedDict()
for i in range(N):
    A = list(input().split())
    if len(A) > 2:
        B = A[0] + " " + A[1]
        if B in order_dict:
            order_dict[B] = int(A[2]) + order_dict.get(B)
        else: order_dict[B] = int(A[2])
    else:
        B = A[0]
        if B in order_dict:
            order_dict[B] = int(A[1]) + order_dict.get(B)
        else: order_dict[B] = int(A[1])
for x in order_dict:
    print(x, order_dict[x])
