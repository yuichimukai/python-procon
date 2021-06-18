#挿入ソート
n = int(input())
A = list(map(int, input().split()))
for i in range(1, n):
    print(' '.join(map(str, A)))
    temp = A[i]
    j = i - 1
    while A[j] > temp and j >= 0:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = temp
print(' '.join(map(str, A)))