S = list(input())
S.append(S[0])
del S[0]
print(S[0] + S[1] + S[2])

#別解
s = input()
print(s[1:] + s[0])

