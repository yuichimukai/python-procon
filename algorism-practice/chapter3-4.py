N = int(input())
A = [*map(int, input().split())]

count = 0
for i in range(N-1):
  j_min = A.index(min(A[i:]), i)
  if A[i] > A[j_min]:
    A[i], A[j_min] = A[j_min], A[i]
    count += 1
print(*A)
print(count)