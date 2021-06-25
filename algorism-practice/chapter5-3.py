#二分探索
#bisectモジュールを使う場合
import bisect

_, S = input(), [*map(int, input().split())]
_, T = input(), [*map(int, input().split())]

def binary_search(S, t):
    return t == S[bisect.bisect_left(S, t)]

print(sum(binary_search(S, t) for t in T))

#使わない場合
_, S = input(), [*map(int, input().split())]
_, T = input(), [*map(int, input().split())]

def binary_search(S, t):
  left, right = 0, len(S)
  while left < right:
    mid = (left + right) // 2
    if S[mid] == t:
      return True
    if S[mid] > t:
      right = mid
    else:
      left = mid + 1
  return False

print(sum(binary_search(S, t) for t in T))


