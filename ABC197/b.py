h,w,x,y=map(int,input().split())
re=0
la=[]
for i in range(h):
    s=input()
    la.append(s)

for j in range(y-1,w):
    if la[x-1][j]=="#":
        break
    else:
        re+=1
for k in range(y-2,-1,-1):
    if la[x-1][k]=="#":
        break
    else:
        re+=1
for j in range(x,h):
    if la[j][y-1]=="#":
        break
    else:
        re+=1
for k in range(x-2,-1,-1):
    if la[k][y-1]=="#":
        break
    else:
        re+=1

print(re)