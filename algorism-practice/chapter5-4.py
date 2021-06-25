#ハッシュ
d = set()
for _ in range(int(input())):
  command, s = input().split()
  if command == "find":
    print("yes" if s in d else "no")
  else:
    d.add(s)