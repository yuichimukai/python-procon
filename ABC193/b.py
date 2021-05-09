INF = 1 << 30
N = int(input())
ans = INF
for i in range(N):
    A, P, X = map(int, input().split())
    if X > A and ans > P:
        ans = P
if ans == INF:
    ans = -1
print(ans)

#別解
n = int(input())
#float型に無限大を表すinfの生成(正の無限大)
ans = float('inf')

for i in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        ans = min(ans, p)

if ans == float('inf'):
    print(-1)
else:
    print(ans)