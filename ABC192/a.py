X = int(input())
goal = X//100*100 + 100
print(goal - X)

#別解
print(100 - (int(input()) % 100))

X = int(input())
N = X % 100
if N == 0: 
    print(100)
else:
    print(100 - N)