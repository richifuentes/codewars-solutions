A = set(map(int, input().split())) # Elements of set A
tests = int(input()) # Number of other sets
result1 = int()
result2 = int()
for i in range(0,tests):
    B = set(map(int, input().split())) # Elements of set B
    if A.issuperset(B) == True: result1 += 1
    elif A.issuperset(B) == False: result2 += 1
if result1 == tests: print('True')
else: print('False')
