def remove_smallest(numbers):
    a = []
    a.extend(numbers)
    if len(a) == 0:
        return a
    elif len(a) == 1:
        a.pop(0)
        return a
    for i in range(len(a)):
        if a[i] == min(a):
            a.pop(i)
            return a
            break
