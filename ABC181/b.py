n = int(input())
ans = 0
for i in range(n):
    a, b = map(int,input().split())
    ans += b * (b+1) // 2 - a * (a-1) // 2
print(ans)

#別解
num = int(input())
ans = 0
for i in range(num):
    a, b = map(int, input().split())
    ans += (a+b)*(b-a+1)//2
print(ans)