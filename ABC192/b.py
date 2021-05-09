S = input()
#重要
#enumerate()関数の引数にイテラルオブジェクトを指定するとインデックス番号、要素が取得できる
#islower,isupperはbool値を返す
is_unreadable = all([c.islower() if i%2==0 else c.isupper() for i,c in enumerate(S)])
if is_unreadable:
    print("Yes")
else:
    print("No")