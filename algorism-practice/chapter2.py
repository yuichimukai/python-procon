R = [int(input()) for i in range(int(input()))]
dfmx = -10 ** 10
mn = 10 ** 10
for i in range(len(R)):
    dfmx = max(R[i] - mn, dfmx)
    mn = min(R[i], mn)
print(dfmx)