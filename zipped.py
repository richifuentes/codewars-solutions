b = list(map(int, input().split()))  # Getting number of students N and Subjects X
N = b[0]  # Student
X = b[1]  # Subjects
students = list()  # List of Students IDs of String type
for i in range(1, N + 1):
    students.append(str(i))
a = list()
for i in range(X):
    a.append(list(zip(students, map(float, input().split()))))
note = float()
for i in range(N):
    note = 0
    for j in range(X):
        b = a[j][i]
        note = note + b[1]
    print(note/X)
