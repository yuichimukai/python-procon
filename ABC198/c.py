import math

R,X,Y=map(int,input().split())
D=math.sqrt(X*X+Y*Y)

if D==R:
  print(1)
elif D<=R+R:
  print(2)
else:
  #εγδΈγ
  print(math.ceil(D/R))
