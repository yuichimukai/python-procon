#線形探索
_, S = input(), input().split()
_, T = input(), input().split()
print(sum(t in S for t in T))