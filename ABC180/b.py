N = int(input())
x = list(map(int, input().split()))
x = [abs(x[i]) for i in range(N)]
#マンハッタン距離
print(sum(x))
#ユークリッド距離
x_sq = [x[i]**2 for i in range(N)]
print(sum(x_sq)**0.5)
#チェビシェフ距離
print(max(x))


#参考
slist = ['3', '4', '5']
# 文字列を整数に変換してsum()実行
sum(int(i) for i in slist)

