tests = int(input()) # Number of tests to run
for i in range(0,tests):
    nom1 = int(input()) # Number of elements in Set
    A = set(map(int, input().split()))
    nom2 = int(input()) # Number of elements in Set
    B = set(map(int, input().split()))
    print(A.issubset(B))
