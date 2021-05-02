x = [1, 2, 3]
print(x)

for i in x:
    print(i)

y = [[1, 2, 3], [4, 5, 6]]
print(y)

for z in y:
    for columns in z:
        print(columns)

q = [[2, 3, 4], [4, 5, 4]]
for i in range(2):
    for j in range(3):
        print(q[i][j])

x = list(input().split())
print(x)
