def solve():
  from itertools import product
  
  n = int(input())
  A = list(map(int,input().split()))
  
  ans = float('INF') #ansを大きい数で初期化
  
  for bit in product((True, False), repeat=n-1):
    bit = list(bit) + [True] #A[N-1]の右隣に常に区切り棒があることとする
    score = 0 #各区間のXOR
    cur = 0 #各区間のOR
    
    for i in range(n): # | -> or
      cur |= A[i]
      if bit[i]:
        #区切り棒が来たら今の区間は終わり
        score ^= cur # ^ -> xor
        cur = 0      #区間のORを0にリセット
      #N番目の区切り棒を追加しているため、最後の区間の処理は特にしない
        
    ans = min(ans, score) #最小値の更新
  
  print(ans)
  
solve()