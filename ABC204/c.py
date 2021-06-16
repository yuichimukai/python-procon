import sys
sys.setrecursionlimit(10000)

#入力
N, M = map(int, input().split())
G = [[] for i in range(N)]
# G[i]は都市iから道路でつながっている都市のリスト
for i in range(M):
  A, B = map(int, input().split())
  G[A-1].append(B-1)

#dfs 
def dfs(v):
  if temp[v]: return
  temp[v] = True
  for vv in G[v]: dfs(vv)

ans = 0

#都市iからスタートする場合
for i in range(N):
  temp = [False]*N
  #temp[j]は都市jに到達可能かどうかを表す
  dfs(i)
  ans += sum(temp)

print(ans)