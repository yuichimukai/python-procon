x = int(input())
print(x)

x = input()

# 文字列を複数の変数に格納
x, y, z = input()
print(x, y, z)


# 整数を複数の変数に格納
x, y = map(int, input().split())
print(x)
print(y)

# 文字列を複数の変数に格納
x, y = input().split()

# リストに整数を格納
x = list(map(int, input().split())

x=[int(i) for i in input().split()]

x, y=[int(input()) for i in range(2)]


x=[int(input()) for i in range(5)]

# 入力行数の指定、リストに整数を格納
rows=int(input())
x=[int(input()) for i in range(rows)]

# 文字列の場合
rows=int(input())
x=[input() for i in range(rows)]

# 整数を2次元リストに格納
x=[list(map(int, input().split())) for i in range(3)]

rows=int(input())
x=[list(map(int, input().split())) for i in range(rows)]
x=[[int(j) for j in input().split()] for i in range(rows)]

x=[]
for i in range(rows):
  x.append(list(map(int, input().split())))
print(x)


# 整数と文字列を複数のリストに格納する
rows=int(input())
number=[]
alphabet=[]
for i in range(rows):
  n, a=input().split()
  number.append(int(n))
  alphabet.append(a)
  print(number)
  print(alphabet)

# 階乗
import math
print(math.factorial(5))

# べき乗
print(10**9)


# 冪根
print(4**0.5)

# 小数点切り捨て除算
print(5//3)

# 小数点切り上げ除算
import math
print(math.ceil(1.1))

# 論理演算
print(True and True)

print(True or False)

print(not False)

x=1
if x=1:
  print("x is 1")
elif x == 2:
  print("x is 2")
else:
  print("x is not 1")


# in演算子
x="Hello world!"
if "e" in x:
  print("e include")
else:
  print("e don't include")

x=["a", "b", "c"]
if "a" in x:
  print("a include")
else:
  print("a don't include")

# 三項演算子
x=1
print("x is 1" if x == 1 else "x is not 1")

x=3
print("x is 1" if x == 1
      else "x is 2" if x == 2
      else "x is 3" if x == 3
      else "other")


# in 演算
x="Hello world!"
print("e include" if "e" in x else "e don't include")



for i in range(5)
  print i

# in を使った繰り返し
x=["a", "b", "c"]
for i in x:
  print(i)

# while文
i=0
while i < 5:
  print(i)
  i += 1
