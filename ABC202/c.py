n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
from collections import Counter

#配列内の数値データをカウントする
count = Counter(a)
ans = 0

for x in c:
    #インデックスは一つさげる必要があるため
    y = x-1
    k = b[y]
    ans += count[k]
print(ans)
