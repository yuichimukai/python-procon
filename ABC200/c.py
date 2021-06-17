N=int(input())
A=list(map(lambda x:int(x)%200,input().split()))
ans=0
for i in range(200):
    num=A.count(i)
    #同じあまりの数の組み合わせの算術 組み合わせのため重複しているものを/2により除く
    ans+=(num*(num-1))/2
print(int(ans))


def main():
    N = int(input())
    A = list(map(int, input().split()))

    R = [x % 200 for x in A]
    cnt = [0] * 200

    ans = 0
    for r in R: 
        ans += cnt[r]
        cnt[r] += 1
    print(ans)


#おまじない 外部からインポートされたときにインポートと同時にじっこうまでされないようにするため
if __name__ == '__main__':
    main()
