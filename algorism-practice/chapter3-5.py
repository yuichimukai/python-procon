N = int(input())
A = input().split()

#バブルソート
def bubble_sort(A, N):
  for i in range(N):
    for j in reversed(range(i+1, N)):
      if A[j][1] < A[j-1][1]:
        A[j-1], A[j] = A[j], A[j-1]

#選択ソート
def selection_sort(A, N):
  for i in range(N-1):
    j_min = A.index(min(A[i:], key=lambda a:a[1]), i)
    A[i], A[j_min] = A[j_min], A[i]

A_bub = A[:]
bubble_sort(A_bub, N)
print(*A_bub)
print("Stable")

#バブルソートは安定ソートであるため選択ソートとバブルソートを比較する
selection_sort(A, N)
print(*A)
print("Stable" if A == A_bub else "Not stable")