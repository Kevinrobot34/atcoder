from collections import defaultdict
MOD = 10**9 + 7
n = int(input())
s = input()

d = defaultdict(int)
for i in range(n):
    d[s[i]] += 1

ans = 1
for c in d:
    ans *= d[c] + 1
    ans %= MOD
ans -= 1
print(ans)
