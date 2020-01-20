from collections import defaultdict
MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for ai in a:
    d[ai] += 1

if n % 2 == 0:
    ans = 1
    for i in range(n//2):
        j = 2*i + 1
        ans *= 2 if d[j] == 2 else 0
        ans %= MOD
else:
    ans = 1 if d[0] == 1 else 0
    for i in range(n//2):
        j = 2 * (i+1)
        ans *= 2 if d[j] == 2 else 0
        ans %= MOD

print(ans)
