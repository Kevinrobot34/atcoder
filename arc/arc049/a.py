s = input()
a, b, c, d = map(int, input().split())
ans = s[:a] + '"' + s[a:b] + '"' + s[b:c] + '"' + s[c:d] + '"' + s[d:]
print(ans)
