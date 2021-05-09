N, K = map(int, input().split())
for i in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        N = str(N)
        s = '200'
        N += s
        N = int(N)
print(N)