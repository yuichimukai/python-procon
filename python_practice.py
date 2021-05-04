x = int(input())
print(x)

x = input()

#文字列を複数の変数に格納
x, y, z = input()
print(x, y, z )


#整数を複数の変数に格納
x, y = map(int, input().split())
print(x)
print(y)

#文字列を複数の変数に格納
x, y = input().split()

#リストに整数を格納
x = list(map(int, input().split())

x = [int(i) for i in input().split()]

x, y = [int(input()) for i in range(2)]


x = [int(input()) for i in range(5)]

#入力行数の指定、リストに整数を格納
rows = int(input())
x = [int(input()) for i in range(rows)]

#文字列の場合
rows = int(input())
x = [input() for i in range(rows)]

#整数を2次元リストに格納
x = [list(map(int, input().split())) for i in range(3)]

rows = int(input())
x = [list(map(int, input().split())) for i in range(rows)]
x = [[int(j) for j in input().split()] for i in range(rows)]

x =[]
for i in range(rows):
  x.append(list(map(int, input().split())))
print(x)


#整数と文字列を複数のリストに格納する
rows = int(input())
number =[]
alphabet = []
for i in range(rows):
  n , a = input().split()
  number.append(int(n))
  alphabet.append(a)
  print(number)
  print(alphabet)






