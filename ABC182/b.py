#Aiの上限1000より大きい数はGCD度は0.2<=AiよりA1のGCD度は少なくとも１より1000より大きい数は考慮しない
N = int(input())
A = list(map(int, input().split()))

ans = -1
mx = 0

#rangeの引数2つ目は含まれないので注意
for x in range(2,1001):
    s = sum(a % x == 0 for a in A)
    if mx < s:
        mx = s
        ans = x
print(ans)

#内包表記
s = sum(a % x == 0 for a in A)
