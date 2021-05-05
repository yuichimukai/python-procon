print(int(2.5))

print("Hello world")

print("foo" + "bat")


# 文字列の繰り返し
print("Helloworld!" * 2)

x = "amc"
print(x[0])

# 文字列の逆順
print(x[::-1])

# 文字列の出現回数
print(x.count("d"))


# 文字列の置換
print(x.replace("mc", "xy"))


# スライス
print(x[1:3])
# 最初のインデックス最後のインデックス省略可
# ステップ数は省略した時１
print(x[:3])

x = ["a", "b", "c"]
print(x[0], x[1])


# 要素追加
x.append("d")

# 探索
print(x.index("c"))

# 取りだし
print(x.pop(1))
# 要素番号指定しない場合は最後の要素が取り出し

# 取り除き
x.remove("a")

# 削除要素
del x[1]
del x[2:4]
# 下記はリスト内すべて削除
del x[:]


# 要素の出現回数
print(x.count("c"))


y = ["a", "b", "c", "d"]
# 要素の結合
print("".join(x))
print(",".join(y))
# 要素のユニーク化
print(list(set(x)))


# 組み込み関数
