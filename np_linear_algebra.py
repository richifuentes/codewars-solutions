import numpy as np
N = int(input()) # The Matrix size
A = list()
for i in range(0,N):
    A[i] = map(float, input().split())

B = np.zeros((N,N))

for x in range(len(A)):
    B[0,0]=A[0]
    B[0,1]=A[1]

print(A)
print(B)
