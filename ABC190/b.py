N, S, D = map(int, input().split())
def check():
    X, Y = map(int, input().split())
    return X < S and Y > D

#一つでもTrueがあれば良いのでany関数を使う
if any(check() for i in range(N)):
    print("Yes")
else:
    print("No")