N,K = map(int, input().split())
A = [0 for i in range(N)]
B = [0 for i in range(N)]
C = []
for i in range(N):
    A[i],B[i] = map(int, input().split())
    C.append([A[i],B[i]])
#昇順に並べ村の数が小さい順に配列を並べる
C.sort()

v = K

for i in range(N):
  #村Kが村iよりも大きいときに友達からB[i]円もらえる
    if v >= C[i][0]:
        v += C[i][1]
    else:
        break

print(v)
