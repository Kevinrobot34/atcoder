n = int(input())
s, t = input().split()

ans = ''.join(s[i] + t[i] for i in range(n))
print(ans)
