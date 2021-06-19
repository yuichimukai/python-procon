N = int(input())
A = list(map(int, input().split()))
ans = 0
# 配列Aの各要素をkeyにとり、出現数をvalueにとるmap
# [-5, 8, 3, -5]の場合→{-5:2, 3:1, 8:1}
element_count_map = {}

# 配列Aの各要素数をmapにカウントしておく
for i in range(N):
  element = A[i]
  if element in element_count_map.keys(): # 既に登録されていればカウントを増やす
    element_count_map[element] += 1
  else:
    element_count_map[element] = 1 # なければ代入する
    
# sortしておくことでi<jのときにelment_list[i]<elment_list[j]を担保できる
elment_list = sorted(list(element_count_map.keys()))

# Aの要素の範囲は-200<=Ai<=200なので多くても400通りくらい
element_list_len = len(elment_list)

for i in range(element_list_len):
  for j in range(i+1, element_list_len):
    # 要素の差分
    diff_square = (elment_list[j] - elment_list[i])**2
    # 上記の差分になる組み合わせの個数
    combination_num = element_count_map[elment_list[j]] * element_count_map[elment_list[i]]
    ans += combination_num * diff_square

print(ans)

#別解

n = int(input())
a = list(map(int, input().split()))
ai = [0] * 420
for i in range(n):
  ai[a[i]+200] += 1

ans = 0

for j in range(410):
  for k in range(j):
    ans += (j - k) ** 2 * (ai[j] * ai[k])
    
print(ans)
