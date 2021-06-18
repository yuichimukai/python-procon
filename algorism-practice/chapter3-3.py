#バブルソート
n = int(input())
A = list(map(int, input().split()))
cnt = 0
flg = 1
while flg:
    flg = 0
    for i in range(n - 1, 0, -1):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            cnt += 1
            flg = 1
print(' '.join(map(str, A)))
print(cnt)