n = int(input())  # Getting number of students
student = dict(); listu = []
for i in range(n):
    b = list(input().split())  # Getting number of students N and Subjects
    student.update(Student=b[0], Maths=float(b[1]), Physics=float(b[2]),Chemistry=float(b[3]))
    listu.insert(i, student)
print(listu)
