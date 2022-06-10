from collections import namedtuple
N = int(input()) #Number of Students in the set.
M = namedtuple('Student',str(input())) #Name of the columns.
A = []
marks = int()
for i in range(0,N):
    A.append(input().split())
for i in range(len(A)):
    globals()["x" + str(i)] = M( int(A[i][0]), int(A[i][1]), str(A[i][2]), int(A[i][3]))
for j in range(0,N):
    args = 'x' + str(j) + '.MARKS'
    marks = marks + eval(args)
print(round(marks/N,3))
